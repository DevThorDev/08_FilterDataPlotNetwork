# -*- coding: utf-8 -*-
###############################################################################
# --- O_00__BaseClass.py ------------------------------------------------------
###############################################################################
import copy, pprint

class BaseClass:
    def __init__(self, inpDat):
        self.idO = 'O_00'
        self.descO = 'Base class'
        self.dIG = inpDat.dI
        self.dITp = copy.deepcopy(self.dIG[0])      # type of base class = 0
        print('Initiated "BaseClass" base object.')

    def __str__(self):
        sIn = ('~'*24 + ' ' + self.descO + ' with ID ' + str(self.idO) + ' ' +
               '~'*24 + '\n' + '~'*80 + '\n')
        return sIn

    def printDType(self):
        print('-'*20, 'Type dictionary:', '-'*20)
        pprint.pprint(self.dITp)
        
    def getValDITp(self, cK):
        if cK in self.dITp:
            return self.dITp[cK]
        else:
            print('ERROR: Key', cK, 'not in type dictionary of', self.descO)
    
    def addToDITp(self, cK, cV):
        if cK in self.dITp:
            print('Assigning key of type dictionary', cK, 'new value', cV)
        else:
            print('Adding entry (', cK, ':', cV, ') to type dictionary')
        self.dITp[cK] = cV
        
###############################################################################
