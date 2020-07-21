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
        sFNetwPlt = (GC.S_NETW_PLOT + '__' + self.dITp['sSelBC2'] + '_' +
                     self.dITp['sSelGT'] + '_' + self.dITp['sTask1'] + '_' +
                     self.dITp['sTask2'] + '.' + GC.S_EXT_PDF)
        self.addToDITp('sFNetwPlt', sFNetwPlt)
        print('Initiated "NetworkPlotter" base object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\n' + '~'*80 + '\n')
        return sIn

    def printDType(self):
        print('-'*20, 'Type dictionary:', '-'*20)
        pprint.pprint(self.dITp)
        
    def createSaveFigure(self, dfrSF):
        lEdgeTrace, lNodeTrace = PF.getTraceLists(self.dITp, dfrSF)
        fig = PF.createFigure(self.dITp, lEdgeTrace, lNodeTrace)
        fig.write_image(GF.joinToPath(self.dITp['pRelPltF'],
                                      self.dITp['sFNetwPlt']))

###############################################################################
