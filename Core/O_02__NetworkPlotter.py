# -*- coding: utf-8 -*-
###############################################################################
# --- O_02__NetworkPlotter.py -------------------------------------------------
###############################################################################
import copy, pprint

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_02__PltFunctions as PF

from Core.O_00__BaseClass import BaseClass

class NetworkPlotter(BaseClass):
    def __init__(self, inpDat, iTp = 2, lITpUpd = [1]):
        super().__init__(inpDat)
        self.idO = 'O_02'
        self.descO = 'Network plotter'
        self.dITp = copy.deepcopy(self.dIG[0])  # type of base class = 0
        for iTpU in lITpUpd + [iTp]:            # updated with types in list
            self.dITp.update(self.dIG[iTpU])
        sPltS = GC.S_NETW_PLOT
        dSFNwPlt = {(sGT, sSelBC2, sSelOp): (sPltS + GC.S_2USC +
                                             self.dITp['lSSelBC2F'][k] +
                                             GC.S_USC + sGT + GC.S_USC +
                                             self.dITp['sTask1'] +
                                             GC.S_USC + self.dITp['sTask2'] +
                                             sSelOp + GC.S_SEP_DOT +
                                             GC.S_EXT_PDF)
                    for sSelOp in self.dITp['lSelOpETr']
                    for k, sSelBC2 in enumerate(self.dITp['lSSelBC2'])
                    for sGT in self.dITp['lSGT']}
        self.addToDITp('dSFNwPlt', dSFNwPlt)
        print('Initiated "NetworkPlotter" base object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\n' + '~'*80 + '\n')
        return sIn

    def printDType(self):
        print('-'*20, 'Type dictionary:', '-'*20)
        pprint.pprint(self.dITp)
        
    def createSaveFigures(self, dDfrSF):
        for cK, sFNwPlt in self.dITp['dSFNwPlt'].items():
            lEdgeTrace, lNodeTrace = PF.getLTrace(self.dITp, dDfrSF[cK])
            fig = PF.createFigure(self.dITp, cK[0], lEdgeTrace, lNodeTrace)
            fig.write_image(GF.joinToPath(self.dITp['pRelPltF'], sFNwPlt))

###############################################################################
