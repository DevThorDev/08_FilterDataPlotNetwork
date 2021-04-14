# -*- coding: utf-8 -*-
###############################################################################
# --- C_00__GenConstants.py ---------------------------------------------------
###############################################################################
import os

# --- general -----------------------------------------------------------------
N_DIG_OBJ_2 = 2
S_SEP_DOT = '.'
S_SEP_P = 'p'
S_SEP_SEMICOL = ';'
S_USC = '_'
S_2USC = S_USC*2
S_WAVE = '~'
S_EQ = '=='
S_L = '<'
S_G = '>'
S_LE = '<='
S_GE = '>='
S_TXT_EQ = 'eq'
S_TXT_L = 'l'
S_TXT_G = 'g'
S_TXT_LE = 'le'
S_TXT_GE = 'ge'

# --- file names, extensions and paths ----------------------------------------
S_OBJINP = 'ObjInput'
S_OBJINP_PRE = 'D_'

S_FILT_DAT = 'FiltDat'
S_COMP_GT = 'CompGT'
S_NETW_PLOT = 'NetworkPlot'

P_REL_G_DATF = os.path.join('..', '..', '12_SysBio02_DataAnalysis',
                            '80_ResultsCSV_Proc', '81_BinaryOps')
P_REL_IN_DATF = P_REL_G_DATF
P_REL_OUT_DATF = os.path.join('..', '..', '12_SysBio02_DataAnalysis',
                              '92_Networkx', '01_Data')
P_REL_PLT_F = os.path.join('..', '..', '12_SysBio02_DataAnalysis',
                           '92_Networkx', '09_Plots')

S_NM_F_INP_GT0 = 'Corr__BinOp_MetD_DvSD_GT0_AllD_PhoD_DvSD_GT0_AllD'
S_NM_F_INP_GT1 = 'Corr__BinOp_MetD_DvSD_GT1_AllD_PhoD_DvSD_GT1_AllD'
S_NM_F_INP_GT5 = 'Corr__BinOp_MetD_DvSD_GT5_AllD_PhoD_DvSD_GT5_AllD'

S_EXT_PY = 'py'
S_EXT_CSV = 'csv'
S_EXT_PDF = 'pdf'

# --- predefined strings ------------------------------------------------------
S_ALL_BIN = 'AllBins'
S_SEL_BIN_2 = 'SelBin2s'

S_SEL = 'sel'
S_THR = 'thr'
S_MIN = 'min'
S_MAX = 'max'
S_AVG = 'avg'
S_INV = 'inv'
S_RGB = 'rgb'

S_GT = 'GT'
S_GT0 = S_GT + '0'
S_GT1 = S_GT + '1'
S_GT5 = S_GT + '5'

S_WT_S = 'WT'
S_PGM_S = 'PGM'
S_SWEET_S = 'SWEET'

S_WT_L = 'wild type'
S_PGM_L = 'pgm mutant'
S_SWEET_L = 'sweet11/12 mutant'

S_MET_D = 'MetD'
S_PHO_D = 'PhoD'
S_MET_F_S = 'metabolites'
S_PHO_F_S = 'phosphopeptides'
S_MET_F_L = 'Metabolites'
S_PHO_F_L = 'Phosphopeptides'

S_PROT = 'Protein'
S_BIN_C_G = 'BinCodeFull'
S_BIN_C_3 = 'BinCode3Dig'
S_BIN_C_2 = 'BinCode2Dig'
S_BIN_C_1 = 'BinCode1Dig'

S_CORR_V = 'CorrV'
S_SPEAR_V = 'SpearV'
S_KEND_V = 'KendV'
S_CORR_P = 'CorrP'
S_SPEAR_P = 'SpearP'
S_KEND_P = 'KendP'
S_N_S_CCD_05 = 'NumSigCcd__SigKW_05'
S_DV_SC_N = 'DvSc_Neg'
S_DV_SC_P = 'DvSc_Pos'
S_DV_SC_PN = 'DvSc_PpN'
S_CI_N = 'CI_Neg'
S_CI_P = 'CI_Pos'
S_CI_PN = 'CI_PpN'
S_OCC_CI_P_M_N = 'sumOccCI_PmN'
S_MET_D_KW_05 = 'MetD__SigKW_05'
S_PHO_D_KW_05 = 'PhoD__SigKW_05'
S_PAT_SIM = 'PatternSimilarity'
S_PAT_E_DST = 'PatternEuclDist'

S_SRT_FLT = 'SortFilt'
S_MEAN = 'Mean'

# --- predefined numbers ------------------------------------------------------
MAX_CLR_VAL = 255
INDEX_DATA_EDGE_ATTR = 2
ATTR_1 = 1
ATTR_2 = 2

THR_2 = 2
THR_3 = 3
THR_4 = 4
THR_5 = 5
THR_6 = 6
THR_7 = 7
THR_8 = 8
THR_9 = 9

K_DIG_RND_04 = 4

# --- predefined dictionaries -------------------------------------------------
D_GT_S = {S_GT0: S_WT_S,
          S_GT1: S_PGM_S,
          S_GT5: S_SWEET_S}
D_GT_L = {S_GT0: S_WT_L,
          S_GT1: S_PGM_L,
          S_GT5: S_SWEET_L}
D_DTYPE = {S_PROT: 'string',
           S_BIN_C_G: 'string',
           S_BIN_C_3: 'string',
           S_BIN_C_2: 'string',
           S_BIN_C_1: 'string'}

# --- bin code 2 lists --------------------------------------------------------
L_BC2_A = ['1.1', '1.3', '5.3', '10.5', '12.1', '12.2', '15.1', '30.11',
           '30.8', '31.1', '33.1', '34.19', '34.5', '34.7']
L_BC2_B = ['1.1', '1.3', '5.3', '10.5', '12.1', '12.2', '15.1', '30.11',
           '30.8', '31.1', '33.1', '34.19', '34.5', '34.7', '30.3', '23.1',
           '4.1', '30.1', '28.99', '2.2', '10.1', '29.6']
L_BC2_C = ['1.1', '1.3', '4.1', '5.3', '8.2', '10.5', '12.1', '12.2', '20.1',
           '20.2', '29.2', '29.4', '29.5', '30.1', '30.11', '30.2', '30.3',
           '33.99', '34.1', '34.19', '34.5']
L_BC2_D = ['1.1', '1.3', '4.1', '5.3', '8.2', '10.5', '12.1', '12.2', '20.1',
           '20.2', '29.2', '29.4', '29.5', '30.1', '30.11', '30.2', '30.3',
           '31.1', '33.99', '34.1', '34.19', '34.5']
L_BC2_E = ['1.1', '1.3', '2.2', '4.1', '5.3', '8.2', '10.5', '12.1', '12.2',
           '20.1', '20.2', '29.2', '29.4', '29.5', '30.1', '30.11', '30.2',
           '30.3', '31.1', '33.99', '34.1', '34.19', '34.5']
L_BC2_F = ['1.1', '1.3', '2.2', '4.1', '5.3', '8.2', '10.5', '12.1', '12.2',
           '20.1', '20.2', '29.2', '29.4', '29.5', '30.1', '30.11', '30.2',
           '30.3', '31.1', '33.99', '34.1', '34.19', '34.5', '34.7']
L_BC2_G = ['1.1', '1.3', '2.2', '4.1', '5.3', '8.2', '10.5', '12.1', '12.2',
           '15.1', '20.1', '20.2', '29.2', '29.4', '29.5', '30.1', '30.11',
           '30.2', '30.3', '30.8', '31.1', '33.1', '33.99', '34.1', '34.19',
           '34.5', '34.7']
L_BC2_H = ['1.1', '1.3', '2.2', '4.1', '8.2', '10.5', '12.1', '12.2', '17.3',
           '30.1', '30.11', '30.2', '30.3', '30.8', '31.1', '33.1', '34.1',
           '34.15', '34.19', '34.5', '34.7']

# --- predefined colours ------------------------------------------------------
CLR_R = 'rgb(255, 0, 0)'
CLR_G = 'rgb(0, 255, 0)'
CLR_B = 'rgb(0, 0, 255)'
CLR_Y = 'rgb(230, 179, 0)'
CLR_DK_1P = 'rgb(204, 0, 102)'
CLR_DK_1G ='rgb(0, 191, 0)'
CLR_DK_2G ='rgb(0, 127, 0)'
CLR_GR_05 = 'rgb(127, 127, 127)'
CLR_8 = '#888'

# --- other constants ---------------------------------------------------------
R04 = 4

# === derived constants =======================================================
D_S_NM_F_INP = {S_GT0: S_NM_F_INP_GT0,
                S_GT1: S_NM_F_INP_GT1,
                S_GT5: S_NM_F_INP_GT5}
L_S_PHO_CL = [S_PROT, S_BIN_C_G, S_BIN_C_3, S_BIN_C_2, S_BIN_C_1]
D_S_CMP = {S_EQ: S_TXT_EQ, S_L: S_TXT_L, S_G: S_TXT_G, S_LE: S_TXT_LE,
           S_GE: S_TXT_GE}
D_BC2 = {'0': [],
         'A': L_BC2_A,
         'B': L_BC2_B,
         'C': L_BC2_C,
         'D': L_BC2_D,
         'E': L_BC2_E,
         'F': L_BC2_F,
         'G': L_BC2_G,
         'H': L_BC2_H}

###############################################################################
