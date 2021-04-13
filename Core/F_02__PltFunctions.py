# -*- coding: utf-8 -*-
###############################################################################
# --- F_02__PltFunctions.py ---------------------------------------------------
###############################################################################
import plotly.graph_objects as go

import Core.C_00__GenConstants as GC
import Core.F_00__GenFunctions as GF
import Core.F_01__SpcFunctions as SF

# --- Functions (networks) ----------------------------------------------------
def getLEdgeTrace(dITp, G, dPos):
    lEdgeTr = []
    lClr = SF.getlClr(dITp, G, iDat = GC.INDEX_DATA_EDGE_ATTR)
    assert len(lClr) == len(G.edges())
    for k, cEdge in enumerate(G.edges()):
        ((x0, y0), (x1, y1)) = (dPos[cEdge[0]], dPos[cEdge[1]])
        dLine = dict(width = dITp['edgeWidth'], color = lClr[k])
        cEdgeTr = go.Scatter(x = [x0, x1], y = [y0, y1], line = dLine,
                             hoverinfo = dITp['hoverInfEdge'],
                             mode = dITp['modeEdge'])
        lEdgeTr.append(cEdgeTr)
    return lEdgeTr

def getNodeTrace(dITp, G, dPos, llSAttr, k):
    lS, lCX, lCY, lNCon, _ = SF.getLNodeInfo(dITp, G, dPos, llSAttr, k)
    dClrBar = dict(x = dITp['lClrBarRelX'][k],
                   thickness = dITp['lClrBarThickn'][k],
                   title = dITp['lClrBarTitleM'][k],
                   xanchor = dITp['lClrBarXAnch'][k],
                   titleside = dITp['lClrBarTSide'][k])
    dMark = dict(showscale = dITp['lShowScaleNode'][k],
                 colorscale = dITp['lClrScaleNode'][k],
                 reversescale = dITp['lRevScaleNode'][k], color = lNCon,
                 size = dITp['lSzMark'][k], colorbar = dClrBar,
                 line_width = dITp['lLwdNode'][k])
    nodeTr = go.Scatter(x = lCX, y = lCY, mode = dITp['lModeNode'][k],
                        hoverinfo = dITp['lHoverInfNode'][k], marker = dMark)
    nodeTr.text = lS
    nodeTr.textfont = dict(size = dITp['lSzTxtNode'][k],
                           color = dITp['lClrTxtNode'][k])
    return nodeTr

def getLTrace(dITp, pdDfr):
    G, llSAttr, dPos = SF.constructNetwork(dITp, pdDfr)
    lEdgeTrace = getLEdgeTrace(dITp, G, dPos)
    dITp['lClrBarTitleM'] = GF.modSClrBar(dITp['lSCol'], dITp['lClrBarTitle'])
    lNodeTrace = []
    for k in range(len(llSAttr)):
        lNodeTrace.append(getNodeTrace(dITp, G, dPos, llSAttr, k))
    return lEdgeTrace, lNodeTrace

def createFigure(dITp, sGT, lEdgeTrace, lNodeTrace):
    lAnnot = [dict(text = dITp['textAnnot'], showarrow = dITp['showArrAnnot'],
                   xref = dITp['xRefAnnot'], yref = dITp['yRefAnnot'],
                   x = dITp['xPosAnnot'], y = dITp['yPosAnnot'])]
    figTtl = dITp['figTitle']
    if sGT in GC.D_GT_L:
        figTtl += ' (' + GC.D_GT_L[sGT] + ')'
    return go.Figure(data = lEdgeTrace + lNodeTrace,
                     layout = go.Layout(title = figTtl,
                                        titlefont_size = dITp['fontSzTitle'],
                                        showlegend = dITp['showLegTitle'],
                                        hovermode = dITp['hoverModeTitle'],
                                        margin = dITp['dMarginTitle'],
                                        annotations = lAnnot,
                                        xaxis = dITp['xAxisAnnot'],
                                        yaxis = dITp['yAxisAnnot']))

###############################################################################
