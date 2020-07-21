# -*- coding: utf-8 -*-
###############################################################################
# --- I_01__InpData.py --------------------------------------------------------
###############################################################################
import os, pprint

from importlib import import_module

import Core.C_00__GenConstants as GC

###############################################################################
class InputData:
    def __init__(self, inpDat, lVals = []):
        dInp = {}
        if type(inpDat) is dict:
            for cKey in inpDat:
                dInp[cKey] = inpDat[cKey]
        elif type(inpDat) is list:
            lKeys = inpDat
            nKeys, nVals = len(lKeys), len(lVals)
            if nKeys == nVals:
                for cIdx in range(nKeys):
                    dInp[lKeys[cIdx]] = lVals[cIdx]
            else:
                print('ERROR: Cannot add to input dictionary.')
                print('Length of keys and values lists:', nKeys, '!=', nVals)
                assert False
        self.dI = dInp
    
    def __str__(self):
        sIn = ('*'*24 + ' "InputData" type ' + '*'*24 +
               '\nInput dictionary:\n' + str(self.dI))
        return sIn

    def addObjTps(self, nmDObjInp):
        nmPre, pyX = GC.S_OBJINP_PRE, GC.S_EXT_PY
        for nmF in os.listdir(nmDObjInp):
            if len(nmF) >= len(nmPre) + self.dI['nDigObj'] + len(pyX):
                if nmF.startswith(nmPre) and nmF.endswith(pyX):
                    nmMod, iTp = nmDObjInp + '.' + nmF[:(-len(pyX) - 1)], 0
                    sBID = nmF[len(nmPre):len(nmPre) + self.dI['nDigObj']]
                    try:
                        iTp = int(sBID)
                        cMod = import_module(nmMod)
                        print('Imported module', nmMod)
                        self.dI[iTp] = getattr(cMod, 'dIO')
                        self.dI[iTp]['iTp'] = iTp
                    except:
                        print('ERROR: Cannot convert', sBID, 'to an integer.')
                        print('Object with type index', iTp, 'not imported.')
                        print('Name of module:', nmMod)
                        assert False

    def yieldOneVal(self, cKey):
        retVal = None
        if cKey in self.dI:
            retVal = self.dI[cKey]
        else:
            print('ERROR: Key', cKey, 'not in input dictionary.')
            assert False
        return retVal
    
    def yieldValList(self, lKeys):
        retList = [None]*len(lKeys)
        for cIdx, cKey in enumerate(lKeys):
            retList[cIdx] = self.yieldOneVal(cKey)
        return retList
    
    def yieldDict(self, lKeys):
        retDict = {}
        for cKey in lKeys:
            retDict[cKey] = self.yieldOneVal(cKey)
        return retDict
    
    def printInputData(self):
        pprint.pprint(self.dI) 

###############################################################################
