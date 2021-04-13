# -*- coding: utf-8 -*-
###############################################################################
# --- F_03__OTpFunctions.py ---------------------------------------------------
###############################################################################
import numpy as np

import networkx as nx

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# --- Functions (filtering) ---------------------------------------------------
def calcFromCVal(dITp, dFlt, lDfr, sSlOp):
    lDfrR = []
    nK, tHd = dFlt[sSlOp]
    # flatten the possibly nested list of DataFrames first
    for k in range(len(tHd) - 1):
        lDfr = GF.flattenIt(lDfr)
    if sSlOp in [GC.S_MAX, GC.S_AVG]:
        # get the min/max/average of all values with same tHd-def. columns
        for cDfr in lDfr:
            if sSlOp in [GC.S_MIN, GC.S_MAX]:
                if sSlOp == GC.S_MIN:
                    cDfr = cDfr[cDfr[nK] == min(cDfr[nK])]
                else:
                    cDfr = cDfr[cDfr[nK] == max(cDfr[nK])]
                if cDfr.shape[0] > 1:
                    cDfr = cDfr.iloc[0, :].to_frame().T
            elif sSlOp == GC.S_AVG:
                cDfr.loc[:, nK] = round(np.mean(cDfr[nK]), GC.K_DIG_RND_04)
                cDfr = cDfr.iloc[0, :].to_frame().T
            lDfrR.append(cDfr)
        return GF.concPdDfrS(lDfrR, ignIdx = True)

def sortAndFilter(dITp, pdDfr, sSlBC2, sSlOp):
    dSrt, dFlt = dITp['dSort'], dITp['dDFilt'][sSlBC2]
    dfrM = pdDfr.copy()
    if dFlt is not None:
        if GC.S_SEL in dFlt:       # filter based on list of attributes
            for cK, cL in dFlt[GC.S_SEL].items():
                if len(cL) > 0:
                    dfrM = dfrM[dfrM[cK].isin(cL)].reset_index(drop = True)
                else:
                    dfrM.reset_index(drop = True)
        if GC.S_THR in dFlt:       # filter based on numeric threshold
            for (sCN, (sCmp, cThr)) in dFlt[GC.S_THR].items():
                if sCmp == GC.S_EQ:
                    dfrM = dfrM[dfrM[sCN] == cThr].reset_index(drop = True)
                elif sCmp == GC.S_L:
                    dfrM = dfrM[dfrM[sCN] < cThr].reset_index(drop = True)
                elif sCmp == GC.S_G:
                    dfrM = dfrM[dfrM[sCN] > cThr].reset_index(drop = True)
                elif sCmp == GC.S_LE:
                    dfrM = dfrM[dfrM[sCN] <= cThr].reset_index(drop = True)
                elif sCmp == GC.S_GE:
                    dfrM = dfrM[dfrM[sCN] >= cThr].reset_index(drop = True)
                else:
                    print('ERROR: Operation "', sCmp, '" not implemented.')
        if sSlOp in dFlt:
            # max. / avg. over all entries with the same col. header key tuple
            lDfr = GF.splitDfr(dfrM, dFlt[sSlOp][1])
            # print('TEMP - dfrM:\n', dfrM)
            # print('TEMP - dFlt:\n', dFlt)
            # print('TEMP - dFlt[', sSlOp, '] =', dFlt[sSlOp])
            # print('TEMP - lDfr:')
            # for cDfr in lDfr:
            #     print(cDfr)
            # print('TEMP - END.')
            dfrM = calcFromCVal(dITp, dFlt, lDfr, sSlOp)
    if dSrt is not None:
        dfrM = dfrM.sort_values(list(dSrt), ascending = list(dSrt.values()),
                                ignore_index = True)
    return dfrM.dropna(subset = list(dFlt[GC.S_THR]))

def compareOverGT(dITp, dDfr, sSlBC2, sSlOp):
    print('Calculating genotype comparison file...')
    dCmpGT, lSMnSrt = {}, [GC.S_MEAN + s for s in dITp['lSrtCmpGT']]
    lSValX = [s + GC.S_USC + sGT for s in dITp['lValCmpGT'] for
              sGT in dITp['lSGT']]
    print('Calculating genotype comparison dictionary for selection', sSlBC2)
    for sGT in dITp['lSGT']:
        cDfr = dDfr[(sGT, sSlBC2, sSlOp)]
        for cI in cDfr.index:
            tKey = tuple(cDfr.loc[cI, dITp['lKeyCmpGT']])
            lVal = list(cDfr.loc[cI, dITp['lValCmpGT']])
            GF.addToDictD(dCmpGT, tKey, sGT, lV = lVal)
            if (cI + 1)%10000 == 0:
                print(cI + 1, 'of', cDfr.shape[0], 'lines processed.')
        print('Calculated genotype comparison dictionary for genotype', sGT)
    dfrCmpGT = GF.iniPdDfr(lSNmC = dITp['lKeyCmpGT'] + lSMnSrt + lSValX,
                           lSNmR = range(1, len(dCmpGT) + 1))
    print('Generated genotype comparison dictionary for selection', sSlBC2)
    print('Filling genotype comparison DataFrame for selection', sSlBC2)
    for (k, (cK, cD)) in enumerate(dCmpGT.items()):
        dfrCmpGT.loc[k + 1, dITp['lKeyCmpGT']] = cK
        lMn = [0.]*len(dITp['lSrtCmpGT'])
        for j in range(len(dITp['lSrtCmpGT'])):
            i = dITp['lValCmpGT'].index(dITp['lSrtCmpGT'][j])
            lMn[j] = np.mean([cL[i] for cL in cD.values()])
        dfrCmpGT.loc[k + 1, lSMnSrt] = lMn
        dfrCmpGT.loc[k + 1, lSValX] = GF.extractFromDictL(cD, dITp['lSGT'])
        if (k + 1)%1000 == 0:
            print(k + 1, 'of', len(dCmpGT), 'lines processed.')
    print('Finished generation of genotype comparison DataFrame.')
    return dfrCmpGT.sort_values(by = lSMnSrt, ascending = False)

# --- Functions (networks) ----------------------------------------------------
def getInfoFromG(dITp, G, cDfr):
    llA = []
    for k in range(len(dITp['lSCol'])):
        llA.append(list(set(cDfr.loc[:, dITp['lSCol'][k]])))
    return llA, nx.kamada_kawai_layout(G)

def constructNetwork(dITp, dfrSF):
    sCA1, sCA2, sNA1 = dITp['sColAttr1'], dITp['sColAttr2'], dITp['sNumAttr1']
    G = nx.convert_matrix.from_pandas_edgelist(dfrSF, source = sCA1,
                                               target = sCA2, edge_attr = sNA1)
    llSAttr, dPos = getInfoFromG(dITp, G, dfrSF)
    return G, llSAttr, dPos

def getlClr(dITp, G, iDat, sRGB = GC.S_RGB):
    lEdgeAt = [cDat[iDat][dITp['sNumAttr1']] for cDat in G.edges.data()]
    minV, maxV = min(lEdgeAt), max(lEdgeAt)
    dClr = {'R': [], 'G': [], 'B': []}
    for x in lEdgeAt:
        for sC in dClr:
            vE, vD = minV, maxV
            if dITp['dOffsClr'][GC.S_INV][sC]:
                vE, vD = maxV, minV
            cC = (dITp['dOffsClr'][GC.S_MIN][sC]*(vD - x)/(vD - vE) +
                  dITp['dOffsClr'][GC.S_MAX][sC]*(x - vE)/(vD - vE))
            dClr[sC].append(cC)
    return [sRGB + '(' + GF.getSClr(dClr['R'][k]) + ', ' +
            GF.getSClr(dClr['G'][k]) + ', ' + GF.getSClr(dClr['B'][k]) + ')'
            for k in range(len(lEdgeAt))]

def getLNodeInfo(dITp, G, dPos, llSAttr, k):
    lAdjInfo = list(G.adjacency())
    assert len(G.nodes()) == len(lAdjInfo)
    lCNdX, lCNdY, lNAdjNd, lTxtAdjNd, lS = [], [], [], [], []
    for j, sNd in enumerate(G.nodes()):
        if sNd in llSAttr[k]:
            lS.append(sNd)
            lCNdX.append(dPos[sNd][0])
            lCNdY.append(dPos[sNd][1])
            nAdj = len(lAdjInfo[j][1])
            lNAdjNd.append(nAdj)
            lTxtAdjNd.append(dITp['lSConNode'][k] + str(nAdj))
    return lS, lCNdX, lCNdY, lNAdjNd, lTxtAdjNd

###############################################################################
