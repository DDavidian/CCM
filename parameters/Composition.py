# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:09:14 2019

@author: Dee Davidian
"""
import numpy as np

class WasteStream(object):
    def __init__(self,):
        self.BAU = {
                "Residual":                {"Garbage": 22,  "Comingled": 0,  "GO":     0.0},
                "FO":                      {"Garbage": 35,  "Comingled": 1,  "GO":     0.2},
                "GO":                      {"Garbage": 1,   "Comingled": 0,  "GO":     91.0},
                "Other organic":           {"Garbage": 24,  "Comingled": 0,  "GO":     3.0},
                "Paper/Cardboard":         {"Garbage": 5,   "Comingled": 37, "GO":     0.0},
                "Plastic":                 {"Garbage": 9,   "Comingled": 8,  "GO":     0.0},
                "Glass":                   {"Garbage": 0,   "Comingled": 43, "GO":     0.0},
                "Metal":                   {"Garbage": 1,   "Comingled": 2,  "GO":     0.0},
                "Contamination":           {"Garbage": 4,   "Comingled": 10, "GO":     5.8},
                }
        self.Generation = {"Generation (kg/hh/week)": {"Garbage": 15.78, "Comingled": 6.52, "GO": 3.21},
                }
        return
    
class Composition(WasteStream):    
    def __init__(self, WS):
        self.WS = WS
        return
    def verification(self):
        self.Garbage = [self.WS.BAU[kk]["Garbage"] for kk in self.WS.BAU.keys()]
        self.Comingled = [self.WS.BAU[kk]["Comingled"] for kk in self.WS.BAU.keys()]
        self.GO = [self.WS.BAU[kk]["GO"] for kk in self.WS.BAU.keys()]
        
        self.testGarbage = np.sum(self.Garbage) == 100
        self.testComingled = np.sum(self.Comingled) == 100
        self.testGO = np.sum(self.GO) == 100
        return

####################################################################################################################################
if __name__== '__main__':
    TT = WasteStream()
    Compo = Composition(TT)
    Compo.verification()
    print("testGarbage= ", Compo.testGarbage, "testComingled= ", Compo.testComingled, "testGO=", Compo.testGO)
