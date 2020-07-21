# -*- coding: utf-8 -*-
###############################################################################
# --- A_00__GenInput.py -------------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- flow control ------------------------------------------------------------
doNetworkPlot = True    # True / False (plotting of network data)

# --- output and debug info ---------------------------------------------------
levelDebugOut = 2       # level of debug output (0: no debug output)

# --- general -----------------------------------------------------------------
nDigObj = GC.N_DIG_OBJ_2    # number of digits reserved for all input objects

# --- file and folder names, extensions ---------------------------------------
sObjInp = GC.S_OBJINP
sObjInpPre = GC.S_OBJINP_PRE

sExtPY = GC.S_EXT_PY
sExtCSV = GC.S_EXT_CSV
sExtPDF = GC.S_EXT_PDF 

# --- predefined strings ------------------------------------------------------
sSel = GC.S_SEL
sThr = GC.S_THR
sMin = GC.S_MIN
sMax = GC.S_MAX
sAvg = GC.S_AVG
sInv = GC.S_INV
sRGB = GC.S_RGB

sMetD = GC.S_MET_D
sPhoD = GC.S_PHO_D

sProt = GC.S_PROT
sBinCG = GC.S_BIN_C_G
sBinC3 = GC.S_BIN_C_3
sBinC2 = GC.S_BIN_C_2
sBinC1 = GC.S_BIN_C_1

sSrtFlt = GC.S_SRT_FLT

lSPhoCl = GC.L_S_PHO_CL
dBinCode2 = GC.D_BC2

# --- predefined numbers ------------------------------------------------------
kMxClrV = GC.MAX_CLR_VAL
kIDtEdgeAttr = GC.INDEX_DATA_EDGE_ATTR
kAttr1 = GC.ATTR_1
kAttr2 = GC.ATTR_2

kDigRnd04 = GC.K_DIG_RND_04

# === create input dictionary =================================================
dictInpG = {# --- flow control
            'doNetworkPlot': doNetworkPlot,
            # --- output and debug info
            'lvlDbg': levelDebugOut,
            # --- general
            'nDigObj': nDigObj,
            # --- file and folder names, extensions
            'sObjInp': sObjInp,
            'sObjInpPre': sObjInpPre,
            'sExtPY': sExtPY,
            'sExtCSV': sExtCSV,
            'sExtPDF': sExtPDF,
            # --- predefined strings
            'sSel': sSel,
            'sThr': sThr,
            'sMin': sMin,
            'sMax': sMax,
            'sAvg': sAvg,
            'sInv': sInv,
            'sRGB': sRGB,
            'sMetD': sMetD,
            'sPhoD': sPhoD,
            'sProt': sProt,
            'sBinCG': sBinCG,
            'sBinC3': sBinC3,
            'sBinC2': sBinC2,
            'sBinC1': sBinC1,
            'sSrtFlt': sSrtFlt,
            'lSPhoCl': lSPhoCl,
            'dBinCode2': dBinCode2,
            # --- predefined numbers
            'kMxClrV': kMxClrV,
            'kIDtEdAt': kIDtEdgeAttr,
            'kAttr1': kAttr1,
            'kAttr2': kAttr2,
            'kDigRnd04': kDigRnd04}

###############################################################################
