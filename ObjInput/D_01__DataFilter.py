# -*- coding: utf-8 -*-
###############################################################################
# --- D_01__DataFilter.py -----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
sOType = 'Data filter (D_01__DataFilter)'
sNmSpec = 'Data filter of the D_01__DataFilter class'

# --- names and paths of files and dirs ---------------------------------------
lSF = ['Red__Corr__BinOp_MetD_DvSD_GT0_AllD_PhoD_DvSD_GT0_AllD',
       'Red__Corr__BinOp_MetD_DvSD_GT1_AllD_PhoD_DvSD_GT1_AllD',
       'Red__Corr__BinOp_MetD_DvSD_GT5_AllD_PhoD_DvSD_GT5_AllD']
pRelDatFIn = GC.P_REL_IN_DATF
pRelDatFOut = GC.P_REL_OUT_DATF

# --- filtering ---------------------------------------------------------------
lSSelBC2 = ['0', 'G']        # 'X'; X in {'A',..., 'G'} or X == '0' (all)
# headers of columns used for filter
# lSColFlt = [GC.S_I_DVCL_PN]
# lSColFlt = [GC.S_I_DVCL_PN, 'MetD_05', 'PhoD_05']
# lSColFlt = [GC.S_I_DVCL_PN, 'SpearV', 'SpearP', 'PatternSimilarity']
lSColFlt = [GC.S_I_DVCL_PN, 'NumSigCcd_05']
# lSColFlt = [GC.S_I_DVCL_PN, 'NumSigCcd_05', 'SpearV', 'SpearP', 'PatternEuclDist']
# threshold values for data in columns used for filter
# lThrVal = [7.25]
# lThrVal = [8.0, 'Y', 'Y']
# lThrVal = [7.25, 0.5, 0.05, 4]
lThrVal = [7.25, 2]
# lThrVal = [7.25, 1, 0.5, 0.05, 1.5]
# list of comparison strings ('==', '<', '>', '<=', '>=')
# lSCmp = [GC.S_GE]
# lSCmp = [GC.S_GE, GC.S_EQ, GC.S_EQ]
# lSCmp = [GC.S_GE, GC.S_GE, GC.S_L, GC.S_GE]
lSCmp = [GC.S_GE, GC.S_GE]
# lSCmp = [GC.S_GE, GC.S_GE, GC.S_GE, GC.S_L, GC.S_LE]

selOpETr = GC.S_AVG             # S_AVG / S_MAX (edge trace operation)

# --- generating lists for comparing genotypes --------------------------------
lKeyCmpGT_PhoD = [GC.S_MET_D, GC.S_PHO_D, GC.S_BIN_C_2]
lValCmpGT_PhoD = [GC.S_DV_CL_PN, GC.S_DV_CL_P, GC.S_SPEAR_V, GC.S_SPEAR_P]
lSrtCmpGT_PhoD = [GC.S_DV_CL_PN, GC.S_DV_CL_P, GC.S_SPEAR_V]
lKeyCmpGT_BC2 = [GC.S_MET_D, GC.S_BIN_C_2]
lValCmpGT_BC2 = [GC.S_DV_CL_PN]
lSrtCmpGT_BC2 = [GC.S_DV_CL_PN]

# === assertions ==============================================================
assert len(lThrVal) == len(lSColFlt) and len(lSCmp) == len(lSColFlt)
lIGT, nFlt = [s.find('_' + GC.S_GT) for s in lSF], len(lSColFlt)
for iGT in lIGT:
    assert iGT >= 0

# === derived values and input processing =====================================
sTask2 = ''
for k, s in enumerate(lSColFlt):
    sTask2 += s + '_' + GC.D_S_CMP[lSCmp[k]] + str(lThrVal[k]) + '_'
sTask2 += selOpETr
sTask2 = sTask2.replace(GC.S_SEP_DOT, GC.S_SEP_P)

lSF = [s + '.' + GC.S_EXT_CSV for s in lSF]
lSGT = [s[(lIGT[k] + 1):min(lIGT[k] + 4, len(s))] for k, s in enumerate(lSF)]

llBC2Sel = [GC.D_BC2[sSelBC2] for sSelBC2 in lSSelBC2]
lSSelBC2F = [GC.S_ALL_BIN]*len(lSSelBC2)
for k, sSelBC2 in enumerate(lSSelBC2):
    if sSelBC2 != '0':
        lSSelBC2F[k] = GC.S_SEL_BIN_2 + sSelBC2
    
dSFFiltS = {(sGT, sSelBC2): GC.S_FILT_DAT + '__' + lSSelBC2F[k] + '_' + sGT
            for k, sSelBC2 in enumerate(lSSelBC2) for sGT in lSGT}
dSFCmpGTS = {sSelBC2: GC.S_COMP_GT + '__' + lSSelBC2F[k] + '_' + '_'.join(lSGT)
             for k, sSelBC2 in enumerate(lSSelBC2)}

dDFilt = {sSelBC2: {GC.S_SEL: {GC.S_BIN_C_2: llBC2Sel[k]},
                    GC.S_THR: {lSColFlt[j]: (lSCmp[j], lThrVal[j]) for j in
                               range(nFlt)}}
          for k, sSelBC2 in enumerate(lSSelBC2)}

# === create input dictionary =================================================
dIO = {# --- general
       'sOType': sOType,
       'sNmSpec': sNmSpec,
       # --- names and paths of files and dirs
       'pRelDatFIn': pRelDatFIn,
       'pRelDatFOut': pRelDatFOut,
       # --- filtering
       'lSColFlt': lSColFlt,
       'lThrVal': lThrVal,
       'lSCmp': lSCmp,
       'selOpETr': selOpETr,
       # --- generating lists for comparing genotypes
       'lKeyCmpGT_PhoD': lKeyCmpGT_PhoD,
       'lValCmpGT_PhoD': lValCmpGT_PhoD,
       'lSrtCmpGT_PhoD': lSrtCmpGT_PhoD,
       'lKeyCmpGT_BC2': lKeyCmpGT_BC2,
       'lValCmpGT_BC2': lValCmpGT_BC2,
       'lSrtCmpGT_BC2': lSrtCmpGT_BC2,
       # === derived values and input processing
       'sTask2': sTask2,
       'lSF': lSF,
       'lSGT': lSGT,
       'llBC2Sel': llBC2Sel,
       'lSSelBC2': lSSelBC2,
       'lSSelBC2F': lSSelBC2F,
       'dSFFiltS': dSFFiltS,
       'dSFCmpGTS': dSFCmpGTS,
       'dDFilt': dDFilt}

###############################################################################
