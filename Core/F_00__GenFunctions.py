# -*- coding: utf-8 -*-
###############################################################################
# --- F_00__GenFunctions.py ---------------------------------------------------
###############################################################################
import os, time, itertools

import numpy as np
import pandas as pd

import Core.C_00__GenConstants as GC

# --- Functions ---------------------------------------------------------------
def startSimu():
    startTime = time.time()
    print('+'*50 + ' START', time.ctime(startTime), '+'*30)
    print('Filter data and plot network')
    # plt.close('all')
    return startTime

def createDir(pF):
    if not os.path.isdir(pF):
        os.mkdir(pF)

def joinToPath(pF = '', nmF = 'Dummy.txt'):
    if len(pF) > 0:
        createDir(pF)
        return os.path.join(pF, nmF)
    else:
        return nmF

def joinDirToPath(pF = '', nmD = 'Directory'):
    if len(pF) > 0:
        pF = os.path.join(pF, nmD)
        createDir(pF)
        return pF
    else:
        return nmD

def getSClr(cClrC, cMult = GC.MAX_CLR_VAL):
    return str(round(cClrC*cMult))

def flattenIt(cIterable, retArr = False):
    itFlat = list(itertools.chain.from_iterable(cIterable))
    if retArr:
        itFlat = np.array(itFlat)
    return itFlat

def readCSV(pF, sepD = ',', iCol = None, dDtype = None, lHStr = [],
            iSp = None, splC = True):
    if dDtype is None and lHStr is not None:
        dDtype = {s: str for s in lHStr}
    pdDfr = pd.read_csv(pF, sep = sepD, index_col = iCol, dtype = dDtype)
    if iSp is not None:
        if splC:
            addIDfr = pdDfr.iloc[:, :iSp]
            return pdDfr.iloc[:, iSp:], addIDfr
        else:
            addIDfrT = pdDfr.iloc[:iSp, :].T
            return pdDfr.iloc[iSp:, :], addIDfrT.T
    else:
        return pdDfr

def concPdDfrS(lPdDfr, concAx = 0, verInt = True, srt = False, ignIdx = False,
               dropAx = None):
    d = pd.concat(lPdDfr, axis = concAx, verify_integrity = verInt, sort = srt,
                  ignore_index = ignIdx)
    if dropAx in [0, 1, 'index', 'columns']:
        d.dropna(axis = dropAx, inplace = True)
    return d

def splitDfr(pdDfr, tHd, j = 0):
    lSubDfr, setV = [], set(pdDfr[tHd[j]])
    for cV in setV:
        lSubDfr.append(pdDfr[pdDfr[tHd[j]] == cV])
    if j == len(tHd) - 1:
        return lSubDfr
    else:
        j += 1
        return [splitDfr(cSubDfr, tHd, j) for cSubDfr in lSubDfr]

def modTitleSClrBar(lSColAttr, lSClrBar):
    assert len(lSColAttr) == len(lSClrBar)
    for k, cS in enumerate(lSColAttr):
        if cS == GC.S_MET_D:
            lSClrBar[k] += (' ' + GC.S_MET_F)
        elif cS == GC.S_PHO_D:
            lSClrBar[k] += (' ' + GC.S_PHO_F)
        else:
            lSClrBar[k] += (' ' + cS)

def printElapsedTimeSim(stT, cT, sPre = 'Time'):
    # calculate and display elapsed time 
    elT = round(cT - stT, GC.R04)
    print(sPre, 'elapsed:', elT, 'seconds, this is', round(elT/60, GC.R04),
          'minutes or', round(elT/3600, GC.R04), 'hours or',
          round(elT/(3600*24), GC.R04), 'days.')

def showElapsedTime(startTime):
    print('-'*80)
    printElapsedTimeSim(startTime, time.time(), 'Time')
    print('+'*3 + ' Current time:', time.ctime(time.time()), '+'*3)
    print('-'*80)

def endSimu(startTime):
    print('-'*80)
    printElapsedTimeSim(startTime, time.time(), 'Total time')
    print('*'*20 + ' DONE', time.ctime(time.time()), '*'*20)

###############################################################################
