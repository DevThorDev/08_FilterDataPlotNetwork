# -*- coding: utf-8 -*-
###############################################################################
# --- M_0__Main.py ------------------------------------------------------------
###############################################################################
import os

import Core.F_00__GenFunctions as GF

from Control.A_00__GenInput import dictInpG
from Core.C_00__GenConstants import S_OBJINP
from Core.I_01__InpData import InputData
from Core.O_01__DataFilter import DataFilter
from Core.O_02__NetworkPlotter import NetworkPlotter

# ### MAIN ####################################################################
startTime = GF.startSimu()
# -----------------------------------------------------------------------------
print('='*80, '\n', '-'*33, 'M_0__Main.py', '-'*33, '\n')
print('Current working directory:', os.getcwd())
inDG = InputData(dictInpG)
inDG.addObjTps(S_OBJINP)
print('Added object types.')

cDatFilt = DataFilter(inDG)
print('Starting filtering...')
dDfrSortFilt = cDatFilt.filterDataFrames()
print('Done filtering', cDatFilt.getValDITp('sTask2'), '.')
if inDG.dI['doNetworkPlot']:
    print('Starting network plotting...')
    cNetwPltr = NetworkPlotter(inDG)
    cNetwPltr.createSaveFigures(dDfrSortFilt)
    print('Done network plot', cNetwPltr.getValDITp('sFNetwPlt'), '...')

# -----------------------------------------------------------------------------
GF.endSimu(startTime)
###############################################################################
