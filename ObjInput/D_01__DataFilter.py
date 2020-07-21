# -*- coding: utf-8 -*-
###############################################################################
# --- D_01__DataFilter.py -----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
sOType = 'Data filter (D_01__DataFilter)'
sNmSpec = 'Data filter of the D_01__DataFilter class'

# --- names and paths of files and dirs ---------------------------------------
sFDat = 'Corr__BinOp_MetD_DvSD_GT0_AllD_PhoD_DvSD_GT0_AllD'
pRelDatFIn = GC.P_REL_DATF_G
pRelDatFOut = GC.P_REL_DATF_NX

# --- filtering ---------------------------------------------------------------
sSelBC2 = 'G'                   # 'X'; X in {'A',..., 'G'}
lSNumAttr = [GC.S_I_DVCL_P, GC.S_CORR]  # S_CORR / S_I_DVCL_P / S_I_DVCL_N 
                                        # S_I_DVCL_PN
lThrNum = [7.5, 0.5]            # numeric threshold values (attr. in lSNumAttr)

selOpETr = GC.S_AVG             # S_AVG / S_MAX (edge trace operation)

# === assertions ==============================================================
assert len(lThrNum) == len(lSNumAttr)
iGT = sFDat.find('_' + GC.S_GT)
assert iGT >= 0

# === derived values and input processing =====================================
lBC2Sel = GC.D_BC2[sSelBC2]
sSelBC2 = GC.S_SEL_BIN_2 + sSelBC2
sSelGT, sTask2 = sFDat[(iGT + 1):min(iGT + 4, len(sFDat))], ''
for k, s in enumerate(lSNumAttr):
    sTask2 += s + '_' + str(lThrNum[k]) + '_'
sTask2 += selOpETr
sTask2 = sTask2.replace(GC.S_SEP_DOT, GC.S_SEP_P)
sFDat += ('.' + GC.S_EXT_CSV)
sFFiltDatS = GC.S_FILT_DAT + '__' + sSelBC2
sFFiltDatE = sTask2 + '__' + sFDat

dFilt = {GC.S_SEL: {GC.S_BIN_C_2: lBC2Sel},
         GC.S_THR: {lSNumAttr[k]: ('>=', lThrNum[k]) for k in
                    range(len(lThrNum))}}


# === create input dictionary =================================================
dIO = {# --- general
       'sOType': sOType,
       'sNmSpec': sNmSpec,
       # --- names and paths of files and dirs
       'pRelDatFIn': pRelDatFIn,
       'pRelDatFOut': pRelDatFOut,
       # --- filtering
       'sSelBC2': sSelBC2,
       'lSNumAttr': lSNumAttr,
       'lThrNum': lThrNum,
       'selOpETr': selOpETr,
       'lBC2Sel': lBC2Sel,
       # === derived values and input processing
       'lBC2Sel': lBC2Sel,
       'sSelBC2': sSelBC2,
       'sSelGT': sSelGT,
       'sTask2': sTask2,
       'sFDat': sFDat,
       'sFFiltDatS': sFFiltDatS,
       'sFFiltDatE': sFFiltDatE,
       'dFilt': dFilt}

###############################################################################
