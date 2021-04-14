# -*- coding: utf-8 -*-
###############################################################################
# --- D_01__DataFilter.py -----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
sOType = 'Data filter (D_01__DataFilter)'
sNmSpec = 'Data filter of the D_01__DataFilter class'

# --- names and paths of files and dirs ---------------------------------------
pRelDatFIn = GC.P_REL_IN_DATF
pRelDatFOut = GC.P_REL_OUT_DATF

# --- filtering ---------------------------------------------------------------
# --- selected bin codes (BinCode2)
lSSelBC2 = ['0', 'H']        # 'X'; X in {'A',..., 'H'} or X == '0' (all)
# --- dictionary containing filter conditions
# CI_PpN_7p25
dFltCnd_1F_CI_PpN_7p25 = {'F1': (GC.S_CI_PN, '>=', 7.25)}
dFltCnd_3F_CI_PpN_7p25 = {'F1': (GC.S_CI_PN, '>=', 7.25),
                          'F2': (GC.S_MET_D_KW_05, '==', 'Y'),
                          'F3': (GC.S_PHO_D_KW_05, '==', 'Y')}
dFltCnd_4F_CI_PpN_7p25 = {'F1': (GC.S_CI_PN, '>=', 7.25),
                          'F2': (GC.S_SPEAR_P, '<', 0.05),
                          'F3': (GC.S_MET_D_KW_05, '==', 'Y'),
                          'F4': (GC.S_PHO_D_KW_05, '==', 'Y')}
# CI_PpN_6p0
dFltCnd_1F_CI_PpN_6p0 = {'F1': (GC.S_CI_PN, '>=', 6.0)}
dFltCnd_3F_CI_PpN_6p0 = {'F1': (GC.S_CI_PN, '>=', 6.0),
                         'F2': (GC.S_MET_D_KW_05, '==', 'Y'),
                         'F3': (GC.S_PHO_D_KW_05, '==', 'Y')}
dFltCnd_4F_CI_PpN_6p0 = {'F1': (GC.S_CI_PN, '>=', 6.0),
                         'F2': (GC.S_SPEAR_P, '<', 0.05),
                         'F3': (GC.S_MET_D_KW_05, '==', 'Y'),
                         'F4': (GC.S_PHO_D_KW_05, '==', 'Y')}
# CI_P_7p25
dFltCnd_1F_CI_P_7p25 = {'F1': (GC.S_CI_P, '>=', 7.25)}
dFltCnd_3F_CI_P_7p25 = {'F1': (GC.S_CI_P, '>=', 7.25),
                        'F2': (GC.S_MET_D_KW_05, '==', 'Y'),
                        'F3': (GC.S_PHO_D_KW_05, '==', 'Y')}
dFltCnd_4F_CI_P_7p25 = {'F1': (GC.S_CI_P, '>=', 7.25),
                        'F2': (GC.S_SPEAR_P, '<', 0.05),
                        'F3': (GC.S_MET_D_KW_05, '==', 'Y'),
                        'F4': (GC.S_PHO_D_KW_05, '==', 'Y')}
# CI_P_6p0
dFltCnd_1F_CI_P_6p0 = {'F1': (GC.S_CI_P, '>=', 6.0)}
dFltCnd_3F_CI_P_6p0 = {'F1': (GC.S_CI_P, '>=', 6.0),
                       'F2': (GC.S_MET_D_KW_05, '==', 'Y'),
                       'F3': (GC.S_PHO_D_KW_05, '==', 'Y')}
dFltCnd_4F_CI_P_6p0 = {'F1': (GC.S_CI_P, '>=', 6.0),
                       'F2': (GC.S_SPEAR_P, '<', 0.05),
                       'F3': (GC.S_MET_D_KW_05, '==', 'Y'),
                       'F4': (GC.S_PHO_D_KW_05, '==', 'Y')}

dFltCnd = dFltCnd_4F_CI_P_6p0

# headers of columns used for filter
# lSColFlt = [GC.S_CI_PN]
# lSColFlt = [GC.S_CI_PN, GC.S_MET_D_KW_05, GC.S_PHO_D_KW_05]
# lSColFlt = [GC.S_CI_PN, GC.S_SPEAR_P, GC.S_MET_D_KW_05, GC.S_PHO_D_KW_05]
# lSColFlt = [GC.S_CI_PN, GC.S_SPEAR_V, GC.S_SPEAR_P, GC.S_PAT_SIM]
# lSColFlt = [GC.S_CI_PN, GC.S_N_S_CCD_05]
# lSColFlt = [GC.S_CI_PN, GC.S_N_S_CCD_05, GC.S_SPEAR_V, GC.S_SPEAR_P, GC.S_PAT_E_DST]
# threshold values for data in columns used for filter
# lThrVal = [7.25]
# lThrVal = [7.25, 'Y', 'Y']
# lThrVal = [7.25, 0.05, 'Y', 'Y']
# lThrVal = [7.25, 0.5, 0.05, 4]
# lThrVal = [7.25, 2]
# lThrVal = [7.25, 1, 0.5, 0.05, 1.5]
# list of comparison strings ('==', '<', '>', '<=', '>=')
# lSCmp = [GC.S_GE]
# lSCmp = [GC.S_GE, GC.S_EQ, GC.S_EQ]
# lSCmp = [GC.S_GE, GC.S_L, GC.S_EQ, GC.S_EQ]
# lSCmp = [GC.S_GE, GC.S_GE, GC.S_L, GC.S_GE]
# lSCmp = [GC.S_GE, GC.S_GE]
# lSCmp = [GC.S_GE, GC.S_GE, GC.S_GE, GC.S_L, GC.S_LE]

# --- generating lists for comparing genotypes --------------------------------
lKeyCmpGT_PhoD = [GC.S_MET_D, GC.S_PHO_D, GC.S_BIN_C_2]
lValCmpGT_PhoD = [GC.S_CI_PN, GC.S_DV_SC_P, GC.S_SPEAR_V, GC.S_SPEAR_P]
lSrtCmpGT_PhoD = [GC.S_CI_PN, GC.S_DV_SC_P, GC.S_SPEAR_V]
lAscCmpGT_PhoD = [False, False, False]
lKeyCmpGT_BC2 = [GC.S_MET_D, GC.S_BIN_C_2]
lValCmpGT_BC2 = [GC.S_CI_PN]
lSrtCmpGT_BC2 = [GC.S_CI_PN]
lAscCmpGT_BC2 = [False]

# === assertions ==============================================================
dSF = GC.D_S_NM_F_INP
lIGT = [s.find(GC.S_USC + GC.S_GT) for s in dSF.values()]
for iGT in lIGT:
    assert iGT >= 0

# === derived values and input processing =====================================
sTask2 = ''
for (sCol, sCmp, cVal) in dFltCnd.values():
    sTask2 += (sCol + GC.S_USC + GC.D_S_CMP[sCmp] + GC.S_USC + str(cVal) +
               GC.S_USC)
sTask2 = sTask2.replace(GC.S_SEP_DOT, GC.S_SEP_P)

lSF = [s + '.' + GC.S_EXT_CSV for s in dSF.values()]
lSGT = [s[(lIGT[k] + 1):min(lIGT[k] + 4, len(s))] for k, s in enumerate(lSF)]

llBC2Sel = [GC.D_BC2[sSelBC2] for sSelBC2 in lSSelBC2]
lSSelBC2F = [GC.S_ALL_BIN]*len(lSSelBC2)
for k, sSelBC2 in enumerate(lSSelBC2):
    if sSelBC2 != '0':
        lSSelBC2F[k] = GC.S_SEL_BIN_2 + sSelBC2

dSFFiltS = {(sGT, sSelBC2): (GC.S_FILT_DAT + GC.S_2USC + lSSelBC2F[k] +
                             GC.S_USC + sGT)
            for k, sSelBC2 in enumerate(lSSelBC2) for sGT in lSGT}
dSFCmpGTS = {sSelBC2: (GC.S_COMP_GT + GC.S_2USC + lSSelBC2F[k] + GC.S_USC +
                       GC.S_USC.join(lSGT))
             for k, sSelBC2 in enumerate(lSSelBC2)}

dDFilt = {sSelBC2: {GC.S_SEL: {GC.S_BIN_C_2: llBC2Sel[k]},
                    GC.S_THR: {t[0]: (t[1], t[2]) for t in dFltCnd.values()}}
          for k, sSelBC2 in enumerate(lSSelBC2)}

# === create input dictionary =================================================
dIO = {# --- general
       'sOType': sOType,
       'sNmSpec': sNmSpec,
       # --- names and paths of files and dirs
       'pRelDatFIn': pRelDatFIn,
       'pRelDatFOut': pRelDatFOut,
       # --- filtering
       'dFltCnd': dFltCnd,
       # --- generating lists for comparing genotypes
       'lKeyCmpGT_PhoD': lKeyCmpGT_PhoD,
       'lValCmpGT_PhoD': lValCmpGT_PhoD,
       'lSrtCmpGT_PhoD': lSrtCmpGT_PhoD,
       'lAscCmpGT_PhoD': lAscCmpGT_PhoD,
       'lKeyCmpGT_BC2': lKeyCmpGT_BC2,
       'lValCmpGT_BC2': lValCmpGT_BC2,
       'lSrtCmpGT_BC2': lSrtCmpGT_BC2,
       'lAscCmpGT_BC2': lAscCmpGT_BC2,
       # === derived values and input processing
       'sTask2': sTask2,
       'dSF': dSF,
       'lSF': lSF,
       'lSGT': lSGT,
       'llBC2Sel': llBC2Sel,
       'lSSelBC2': lSSelBC2,
       'lSSelBC2F': lSSelBC2F,
       'dSFFiltS': dSFFiltS,
       'dSFCmpGTS': dSFCmpGTS,
       'dDFilt': dDFilt}

###############################################################################
