# -*- coding: utf-8 -*-
###############################################################################
# --- D_00__BaseClass.py -----------------------------------------------------
###############################################################################
import Core.C_00__GenConstants as GC

# --- general -----------------------------------------------------------------
sOType = 'Base class (D_00__BaseClass)'
sNmSpec = 'Base class of the D_00__BaseClass class'

# --- data specific -----------------------------------------------------------
cSep = GC.S_SEP_SEMICOL

# --- filtering / plotting core input -----------------------------------------
sNumAttr1 = GC.S_CI_PN          # 1st numeric attribute (used as plot property)

sColAttr1 = GC.S_MET_D          # GC.S_MET_D
sColAttr2 = GC.S_BIN_C_2        # GC.S_PHO_D / GC.S_BIN_C_2

lSelOpETr = [GC.S_AVG, GC.S_MAX]    # operations on filtered data

# --- sorting -----------------------------------------------------------------
dSort = {sColAttr1: True,       # column header (string 1): ascending (bool)
         sColAttr2: True,       # column header (string 2): ascending (bool)
         sNumAttr1: False}      # column header (num. 1): descending (bool)

# === derived values and input processing =====================================
sTask1 = sColAttr1 + GC.S_USC + sColAttr2 + GC.S_USC
lSCol = [sColAttr1, sColAttr2]

# === create input dictionary =================================================
dIO = {# --- general
       'sOType': sOType,
       'sNmSpec': sNmSpec,
       # --- data specific
       'cSep': cSep,
       # --- filtering /plotting core input
       'sNumAttr1': sNumAttr1,
       'sColAttr1': sColAttr1,
       'sColAttr2': sColAttr2,
       'lSelOpETr': lSelOpETr,
       # --- sorting
       'dSort': dSort,
       # === derived values and input processing
       'sTask1': sTask1,
       'lSCol': lSCol}

###############################################################################
