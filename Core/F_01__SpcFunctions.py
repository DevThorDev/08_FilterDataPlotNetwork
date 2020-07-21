# -*- coding: utf-8 -*-
###############################################################################
# --- F_03__OTpFunctions.py ---------------------------------------------------
###############################################################################
import numpy as np

import networkx as nx

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF

# --- Functions (filtering) ---------------------------------------------------
def calcFromCVal(dITp, lDfr):
    cOp, lDfrR = dITp['selOpETr'], []
    numK, tHd = dITp['dFilt'][cOp]
    # flatten the possibly nested list of DataFrames first
    for k in range(len(tHd) - 1):
        lDfr = GF.flattenIt(lDfr)
    if cOp in [GC.S_MAX, GC.S_AVG]:
        # get the maximum or average of all values with same tHd-def. columns
        for cDfr in lDfr:
            if cOp == GC.S_MAX:
                cDfr = cDfr[cDfr[numK] == max(cDfr[numK])]
                if cDfr.shape[0] > 1:
                    cDfr = cDfr.iloc[0, :].to_frame().T
            elif cOp == GC.S_AVG:
                cDfr.loc[:, numK] = round(np.mean(cDfr[numK]), GC.K_DIG_RND_04)
                cDfr = cDfr.iloc[0, :].to_frame().T
            lDfrR.append(cDfr)
        return GF.concPdDfrS(lDfrR, ignIdx = True)

def sortAndFilter(dITp, pdDfr):
    cOp, dSrt, dFlt = dITp['selOpETr'], dITp['dSort'], dITp['dFilt']
    dfrM = pdDfr.copy()
    if dFlt is not None:
        if GC.S_SEL in dFlt:       # filter based on list of attributes
            for cK, cL in dFlt[GC.S_SEL].items():
                dfrM = dfrM[dfrM[cK].isin(cL)].reset_index(drop = True)
        if GC.S_THR in dFlt:       # filter based on numeric threshold
            for (sCN, (sCmp, cThr)) in dFlt[GC.S_THR].items():
                if sCmp == '>=':
                    dfrM = dfrM[dfrM[sCN] >= cThr].reset_index(drop = True)
                elif sCmp == '<=':
                    dfrM = dfrM[dfrM[sCN] <= cThr].reset_index(drop = True)
                else:
                    print('ERROR: Operation "', sCmp, '" not implemented.')
        if cOp in dFlt:
            # max. / avg. over all entries with the same col. header key tuple
            dfrM = calcFromCVal(dITp, GF.splitDfr(dfrM, dFlt[cOp][1]))
    if dSrt is not None:
        dfrM = dfrM.sort_values(list(dSrt), ascending = list(dSrt.values()),
                                ignore_index = True)
    return dfrM.dropna(subset = list(dFlt[GC.S_THR]))

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
