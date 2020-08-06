# -*- coding: utf-8 -*-
###############################################################################
# --- O_01__DataFilter.py -----------------------------------------------------
###############################################################################
import copy, pprint

import pandas as pd

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF

from Core.O_00__BaseClass import BaseClass

class DataFilter(BaseClass):
    def __init__(self, inpDat, iTp = 1, lITpUpd = []):
        super().__init__(inpDat)
        self.idO = 'O_01'
        self.descO = 'Data filter'
        self.dITp = copy.deepcopy(self.dIG[0])  # type of base class = 0
        for iTpU in lITpUpd + [iTp]:            # updated with types in list
            self.dITp.update(self.dIG[iTpU])
        dSFInp = {(sGT, sSelBC2): self.dITp['lSF'][k]
                  for sSelBC2 in self.dITp['lSSelBC2']
                  for k, sGT in enumerate(self.dITp['lSGT'])}
        dSFFilt = {(sGT, sSelBC2): (self.dITp['dSFFiltS'][(sGT, sSelBC2)] +
                                    '_' + self.dITp['sTask1'] + '_' +
                                    self.dITp['sTask2'] + '.' + GC.S_EXT_CSV)
                   for sSelBC2 in self.dITp['lSSelBC2']
                   for k, sGT in enumerate(self.dITp['lSGT'])}
        self.addToDITp('dSFInp', dSFInp)
        self.addToDITp('dSFFilt', dSFFilt)
        print('Initiated "DataFilter" base object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\n' + '~'*80 + '\n')
        return sIn

    def printDType(self):
        print('-'*20, 'Type dictionary:', '-'*20)
        pprint.pprint(self.dITp)
    
    def filterDataFrames(self):
        dDfrSF = {}
        for ((sGT, sSelBC2), sFFilt) in self.dITp['dSFFilt'].items():
            pFIn = GF.joinToPath(self.dITp['pRelDatFIn'],
                                 self.dITp['dSFInp'][(sGT, sSelBC2)])
            dfrIn = pd.read_csv(pFIn, sep = self.dITp['cSep'])
            tCA = (self.dITp['sColAttr1'], self.dITp['sColAttr2'])
            tNACA = (self.dITp['sNumAttr1'], tCA)
            self.dITp['dDFilt'][sSelBC2][self.dITp['selOpETr']] = tNACA
            dfrSF = SF.sortAndFilter(self.dITp, dfrIn, sSelBC2)
            pFOut = GF.joinToPath(self.dITp['pRelDatFOut'], sFFilt)
            print(dfrSF.shape[0], 'lines has filtered data frame with key',
                  (sGT, sSelBC2), '.')
            dfrSF.to_csv(pFOut, sep = self.dITp['cSep'])
            dDfrSF[(sGT, sSelBC2)] = dfrSF
        return dDfrSF

###############################################################################
