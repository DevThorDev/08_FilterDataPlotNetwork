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
        self.addToDITp('sFFiltDat', (self.dITp['sFFiltDatS'] + '_' +
                                     self.dITp['sTask1'] + '_' +
                                     self.dITp['sFFiltDatE']))
        print('Initiated "DataFilter" base object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\n' + '~'*80 + '\n')
        return sIn

    def printDType(self):
        print('-'*20, 'Type dictionary:', '-'*20)
        pprint.pprint(self.dITp)
    
    def filterDataFrame(self):
        pFIn = GF.joinToPath(self.dITp['pRelDatFIn'], self.dITp['sFDat'])
        dfrIn = pd.read_csv(pFIn, sep = self.dITp['cSep'])
        t = (self.dITp['sColAttr1'], self.dITp['sColAttr2'])
        self.dITp['dFilt'][self.dITp['selOpETr']] = (self.dITp['sNumAttr1'], t)
        dfrSF = SF.sortAndFilter(self.dITp, dfrIn)
        pFOut = GF.joinToPath(self.dITp['pRelDatFOut'], self.dITp['sFFiltDat'])
        dfrSF.to_csv(pFOut, sep = self.dITp['cSep'])
        return dfrSF

###############################################################################
