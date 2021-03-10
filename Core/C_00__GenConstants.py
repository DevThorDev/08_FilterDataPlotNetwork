# -*- coding: utf-8 -*-
###############################################################################
# --- C_00__GenConstants.py ---------------------------------------------------
###############################################################################
import os

# --- filter ------------------------------------------------------------------
S_I_DVCL_P = 'DvClP'
S_I_DVCL_PN = 'DvClPN'
S_ALL_BIN = 'AllBins'
S_SEL_BIN_2 = 'SelBin2s'
S_SEL_BIN_2_G = S_SEL_BIN_2 + 'G27'

# --- general -----------------------------------------------------------------
N_DIG_OBJ_2 = 2
S_SEP_DOT = '.'
S_SEP_P = 'p'
S_SEP_SEMICOL = ';'
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
                            '11_ResultCSV_GT015', '21_R_81_BinaryOps')
P_REL_IN_DATF = os.path.join('..', '..', '12_SysBio02_DataAnalysis',
                             '92_Networkx', '00_BO_Input')
P_REL_OUT_DATF = os.path.join('..', '..', '12_SysBio02_DataAnalysis',
                              '92_Networkx', '01_Data')
P_REL_PLT_F = os.path.join('..', '..', '12_SysBio02_DataAnalysis',
                           '92_Networkx', '09_Plots')

S_EXT_PY = 'py'
S_EXT_CSV = 'csv'
S_EXT_PDF = 'pdf'

# --- predefined strings ------------------------------------------------------
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
S_BIN_C_G = 'BinCode'
S_BIN_C_3 = 'BinCode3'
S_BIN_C_2 = 'BinCode2'
S_BIN_C_1 = 'BinCode1'

S_CORR_V = 'CorrV'
S_SPEAR_V = 'SpearV'
S_KEND_V = 'KendV'
S_CORR_P = 'CorrP'
S_SPEAR_P = 'SpearP'
S_KEND_P = 'KendP'
S_N_S_CCD_01 = 'NumSigCcd_01'
S_N_S_CCD_05 = 'NumSigCcd_05'
S_N_S_CCD_10 = 'NumSigCcd_10'
S_DV_SC_N = 'DvScN'
S_DV_SC_P = 'DvScP'
S_DV_SC_PN = 'DvScPN'
S_DV_CL_N = 'DvClN'
S_DV_CL_P = 'DvClP'
S_DV_CL_PN = 'DvClPN'
S_P_M_N = 'PmN'
S_MET_D_01 = 'MetD_01'
S_MET_D_05 = 'MetD_05'
S_MET_D_10 = 'MetD_10'
S_PHO_D_01 = 'PhoD_01'
S_PHO_D_05 = 'PhoD_05'
S_PHO_D_10 = 'PhoD_10'
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
         'G': L_BC2_G}

###############################################################################
