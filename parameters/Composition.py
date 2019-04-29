# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:09:14 2019

@author: Dee Davidian
"""
import numpy as np

class WasteComposition(object):
    def __init__(self,):
        self.Waste_Composition = {
                "Garbage":   {"Residual": 22., "FO": 35., "GO": 1., "Other_Organic": 24.,"Paper/Cardboard": 5., "Plastic": 9., "Glass": 0.,"Metal": 1.,"Other": 4.},
                "Comingled": {"Residual": 0., "FO": 1., "GO": 0., "Other_Organic": 0.,"Paper/Cardboard": 37., "Plastic": 8., "Glass": 43.,"Metal": 2.,"Other": 10.},
                "GO":        {"Residual": 0., "FO": 0.2, "GO": 91., "Other_Organic": 3.,"Paper/Cardboard": 0., "Plastic": 0., "Glass": 0.,"Metal": 0.,"Other": 5.8},
                "FO":        {"Residual": 100., "FO": 0., "GO": 0., "Other_Organic": 0.,"Paper/Cardboard": 0., "Plastic": 0., "Glass": 0.,"Metal": 0.,"Other": 0.},
                                }
        self.Generation = {"Generation (kg/hh/week)": {"Garbage": 15.78, "Comingled": 6.52, "GO": 3.21},
                }
        return
    def verification(self):
        for wc in self.Waste_Composition:
            total = [self.Waste_Composition[wc][typetype] for typetype in self.Waste_Composition[wc]]
            test = np.sum(total) #== 100
            print("test ", wc, " sum=100", test)
        return

####################################################################################################################################
if __name__== '__main__':
    TT = WasteComposition()
    TT.verification()
