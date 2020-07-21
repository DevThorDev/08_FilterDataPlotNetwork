# -*- coding: utf-8 -*-
###############################################################################
# --- D_02__NetworkPlotter.py -------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
sOType = 'Data filter (D_02__NetworkPlotter)'
sNmSpec = 'Data filter of the D_02__NetworkPlotter class'

# --- names and paths of files and dirs ---------------------------------------
pRelPltF = GC.P_REL_PLT_F
sFNetwPlt = GC.S_NETW_PLOT + '.' + GC.S_EXT_PDF

# --- predefined colours ------------------------------------------------------
clrR = GC.CLR_R
clrG = GC.CLR_G
clrB = GC.CLR_B
clrY = GC.CLR_Y
clrDk1P = GC.CLR_DK_1P
clrDk1G = GC.CLR_DK_1G
clrDk2G = GC.CLR_DK_2G
clrGr05 = GC.CLR_GR_05
clr8 = GC.CLR_8

# --- edge input --------------------------------------------------------------
edgeWidth = 0.5
hoverInfEdge = 'none'
modeEdge = 'lines'
dOffsClr = {GC.S_MIN: {'R': 0.4, 'G': 0., 'B': 0.2},
            GC.S_MAX: {'R': 0.8, 'G': 0.8, 'B': 0.8},
            GC.S_INV: {'R': True, 'G': True, 'B': True}}

# --- node input --------------------------------------------------------------
lwdNodeAttr1 = 1
lwdNodeAttr2 = 1.5
hoverInfNodeAttr1 = 'text'
hoverInfNodeAttr2 = 'text'
sConNodeAttr1 = '# of connections: '
sConNodeAttr2 = '# of connections: '
modeNodeAttr1 = 'markers+text'
modeNodeAttr2 = 'markers+text'
szTxtNodeAttr1 = 4
szTxtNodeAttr2 = 5
clrTxtNodeAttr1 = clrDk1P
clrTxtNodeAttr2 = clrR

# --- node scale input --------------------------------------------------------
showScaleNodeAttr1 = True
showScaleNodeAttr2 = True
clrScaleNodeAttr1 = 'YlGnBu'
clrScaleNodeAttr2 = 'YlGnBu'
revScaleNodeAttr1 = True
revScaleNodeAttr2 = True
szMarkAttr1 = 12
szMarkAttr2 = 16

# --- colour bar input --------------------------------------------------------
clrBarRelXAttr1 = -0.15
clrBarRelXAttr2 = 1.02
clrBarThicknAttr1 = 15
clrBarThicknAttr2 = 15
clrBarTitleAttr1 = 'Node Connections of'
clrBarTitleAttr2 = 'Node Connections of'
clrBarXAnchAttr1 = 'left'
clrBarXAnchAttr2 = 'left'
clrBarTSideAttr1 = 'right'
clrBarTSideAttr2 = 'right'

# --- title input -------------------------------------------------------------
figTitle = ('<br>Network graph: Metabolites and phosphopeptides' +
            ' (avg. over BinCode2 groups) with similar behaviour (WT)')
fontSzTitle = 11
showLegTitle = False
hoverModeTitle = 'closest'
dMarginTitle = dict(b = 20, l = 5, r = 5, t = 40)

# --- annotations input -------------------------------------------------------
textAnnot = 'Dark purple'
textAnnot += ' edge colour corresonds to higher confidence of connection'
showArrAnnot = False
xRefAnnot = 'paper'
yRefAnnot = 'paper'
xPosAnnot = 0.005
yPosAnnot = -0.002
xAxisAnnot = dict(showgrid = False, zeroline = False, showticklabels = False)
yAxisAnnot = dict(showgrid = False, zeroline = False, showticklabels = False)

# === derived values and input processing =====================================
lLwdNode = [lwdNodeAttr1, lwdNodeAttr2]
lHoverInfNode = [hoverInfNodeAttr1, hoverInfNodeAttr2]
lSConNode = [sConNodeAttr1, sConNodeAttr2]
lModeNode = [modeNodeAttr1, modeNodeAttr2]
lSzTxtNode = [szTxtNodeAttr1, szTxtNodeAttr2]
lClrTxtNode = [clrTxtNodeAttr1, clrTxtNodeAttr2]
lShowScaleNode = [showScaleNodeAttr1, showScaleNodeAttr2]
lClrScaleNode = [clrScaleNodeAttr1, clrScaleNodeAttr2]
lRevScaleNode = [revScaleNodeAttr1, revScaleNodeAttr2]
lSzMark = [szMarkAttr1, szMarkAttr2]
lClrBarRelX = [clrBarRelXAttr1, clrBarRelXAttr2]
lClrBarThickn = [clrBarThicknAttr1, clrBarThicknAttr2]
lClrBarTitle = [clrBarTitleAttr1, clrBarTitleAttr2]
lClrBarXAnch = [clrBarXAnchAttr1, clrBarXAnchAttr2]
lClrBarTSide = [clrBarTSideAttr1, clrBarTSideAttr2]

# === create input dictionary =================================================
dIO = {# --- general
       'sOType': sOType,
       'sNmSpec': sNmSpec,
       # --- names and paths of files and dirs
       'pRelPltF': pRelPltF,
       'sFNetwPlt': sFNetwPlt,
       # --- predefined colours
       'clrR': clrR,
       'clrG': clrG,
       'clrB': clrB,
       'clrY': clrY,
       'clrDk1P': clrDk1P,
       'clrDk1G': clrDk1G,
       'clrDk2G': clrDk2G,
       'clrGr05': clrGr05,
       'clr8': clr8,
       # --- edge input
       'edgeWidth': edgeWidth,
       'hoverInfEdge': hoverInfEdge,
       'modeEdge': modeEdge,
       'dOffsClr': dOffsClr,
       # --- node input
       'lwdNodeAttr1': lwdNodeAttr1,
       'lwdNodeAttr2': lwdNodeAttr2,
       'hoverInfNodeAttr1': hoverInfNodeAttr1,
       'hoverInfNodeAttr2': hoverInfNodeAttr2,
       'sConNodeAttr1': sConNodeAttr1,
       'sConNodeAttr2': sConNodeAttr2,
       'modeNodeAttr1': modeNodeAttr1,
       'modeNodeAttr2': modeNodeAttr2,
       'szTxtNodeAttr1': szTxtNodeAttr1,
       'szTxtNodeAttr2': szTxtNodeAttr2,
       'clrTxtNodeAttr1': clrTxtNodeAttr1,
       'clrTxtNodeAttr2': clrTxtNodeAttr2,
       # --- node scale input
       'showScaleNodeAttr1': showScaleNodeAttr1,
       'showScaleNodeAttr2': showScaleNodeAttr2,
       'clrScaleNodeAttr1': clrScaleNodeAttr1,
       'clrScaleNodeAttr2': clrScaleNodeAttr2,
       'revScaleNodeAttr1': revScaleNodeAttr1,
       'revScaleNodeAttr2': revScaleNodeAttr2,
       'szMarkAttr1': szMarkAttr1,
       'szMarkAttr2': szMarkAttr2,
       # --- colour bar input
       'clrBarRelXAttr1': clrBarRelXAttr1,
       'clrBarRelXAttr2': clrBarRelXAttr2,
       'clrBarThicknAttr1': clrBarThicknAttr1,
       'clrBarThicknAttr2': clrBarThicknAttr2,
       'clrBarTitleAttr1': clrBarTitleAttr1,
       'clrBarTitleAttr2': clrBarTitleAttr2,
       'clrBarXAnchAttr1': clrBarXAnchAttr1,
       'clrBarXAnchAttr2': clrBarXAnchAttr2,
       'clrBarTSideAttr1': clrBarTSideAttr1,
       'clrBarTSideAttr2': clrBarTSideAttr2,
       # --- title input
       'figTitle': figTitle,
       'fontSzTitle': fontSzTitle,
       'showLegTitle': showLegTitle,
       'hoverModeTitle': hoverModeTitle,
       'dMarginTitle': dMarginTitle,
       # --- annotations input
       'textAnnot': textAnnot,
       'showArrAnnot': showArrAnnot,
       'xRefAnnot': xRefAnnot,
       'yRefAnnot': yRefAnnot,
       'xPosAnnot': xPosAnnot,
       'yPosAnnot': yPosAnnot,
       'xAxisAnnot': xAxisAnnot,
       'yAxisAnnot': yAxisAnnot,
       # === derived values and input processing
       'lLwdNode': lLwdNode,
       'lHoverInfNode': lHoverInfNode,
       'lSConNode': lSConNode,
       'lModeNode': lModeNode,
       'lSzTxtNode': lSzTxtNode,
       'lClrTxtNode': lClrTxtNode,
       'lShowScaleNode': lShowScaleNode,
       'lClrScaleNode': lClrScaleNode,
       'lRevScaleNode': lRevScaleNode,
       'lSzMark': lSzMark,
       'lClrBarRelX': lClrBarRelX,
       'lClrBarThickn': lClrBarThickn,
       'lClrBarTitle': lClrBarTitle,
       'lClrBarXAnch': lClrBarXAnch,
       'lClrBarTSide': lClrBarTSide}

###############################################################################
