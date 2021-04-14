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
        self.dITp['lKeyCmpGT'] = self.dITp['lKeyCmpGT_PhoD']
        self.dITp['lValCmpGT'] = self.dITp['lValCmpGT_PhoD']
        self.dITp['lSrtCmpGT'] = self.dITp['lSrtCmpGT_PhoD']
        self.dITp['lAscCmpGT'] = self.dITp['lAscCmpGT_PhoD']
        if self.dITp['sColAttr2'] == GC.S_BIN_C_2:
            self.dITp['lKeyCmpGT'] = self.dITp['lKeyCmpGT_BC2']
            self.dITp['lValCmpGT'] = self.dITp['lValCmpGT_BC2']
            self.dITp['lSrtCmpGT'] = self.dITp['lSrtCmpGT_BC2']
            self.dITp['lAscCmpGT'] = self.dITp['lAscCmpGT_BC2']
        dSFInp = {(sGT, sSelBC2): self.dITp['lSF'][k]
                  for sSelBC2 in self.dITp['lSSelBC2']
                  for k, sGT in enumerate(self.dITp['lSGT'])}
        dSFFilt = {(sGT, sSelBC2, sSelOp):
                   (self.dITp['dSFFiltS'][(sGT, sSelBC2)] + GC.S_USC +
                    self.dITp['sTask1'] + GC.S_USC + self.dITp['sTask2'] +
                   sSelOp + GC.S_SEP_DOT + GC.S_EXT_CSV)
                   for sSelOp in self.dITp['lSelOpETr']
                   for sSelBC2 in self.dITp['lSSelBC2']
                   for sGT in self.dITp['lSGT']}
        dSFCmpGT = {(sSelBC2, sSelOp):
                    (self.dITp['dSFCmpGTS'][sSelBC2] + GC.S_USC +
                     self.dITp['sTask1'] + GC.S_USC + self.dITp['sTask2'] +
                     sSelOp + GC.S_SEP_DOT + GC.S_EXT_CSV)
                    for sSelOp in self.dITp['lSelOpETr']
                    for sSelBC2 in self.dITp['lSSelBC2']}
        self.addToDITp('dSFInp', dSFInp)
        self.addToDITp('dSFFilt', dSFFilt)
        self.addToDITp('dSFCmpGT', dSFCmpGT)
        print('Initiated "DataFilter" base object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\n' + '~'*80 + '\n')
        return sIn

    def printDType(self):
        print('-'*20, 'Type dictionary:', '-'*20)
        pprint.pprint(self.dITp)

    def filterDataFrames(self):
        dDfrSF, dDTp = {}, GC.D_DTYPE
        for ((sGT, sSelBC2, sSelOp), sFFilt) in self.dITp['dSFFilt'].items():
            pFIn = GF.joinToPath(self.dITp['pRelDatFIn'],
                                 self.dITp['dSFInp'][(sGT, sSelBC2)])
            dfrIn = pd.read_csv(pFIn, sep = self.dITp['cSep'], dtype = dDTp)
            tCA = (self.dITp['sColAttr1'], self.dITp['sColAttr2'])
            tNACA = (self.dITp['sNumAttr1'], tCA)
            self.dITp['dDFilt'][sSelBC2][sSelOp] = tNACA
            dfrSF = SF.sortAndFilter(self.dITp, dfrIn, sSelBC2, sSelOp)
            pFOut = GF.joinToPath(self.dITp['pRelDatFOut'], sFFilt)
            print(dfrSF.shape[0], 'lines has filtered data frame with key',
                  (sGT, sSelBC2, sSelOp), '.')
            dfrSF.to_csv(pFOut, sep = self.dITp['cSep'])
            dDfrSF[(sGT, sSelBC2, sSelOp)] = dfrSF
        for ((sSelBC2, sSelOp), sFCmpGT) in self.dITp['dSFCmpGT'].items():
            dfrCmpGT = SF.compareOverGT(self.dITp, dDfrSF, sSelBC2, sSelOp)
            pFOut = GF.joinToPath(self.dITp['pRelDatFOut'], sFCmpGT)
            dfrCmpGT.to_csv(pFOut, sep = self.dITp['cSep'])
        return dDfrSF

###############################################################################
