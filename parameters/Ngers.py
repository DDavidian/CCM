# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:22:28 2019

@author: Dee Davidian
"""

class Waste_Composition_table(object):
    def __init__(self,):
                self.waste_comp = {
                        "FO":                ["Food"],
                        "GO":                ["Garden", "Wood",],
                        "Paper/Cardboard":   ["Paper/Cardboard"],
                        "Plastic":           ["Inert"],
                        "Glass":             ["Inert"],
                        "Residual":          ["Mixed MSW"],
                        "Metal":             ["Inert"],
                        "Other":             ["Other", "Textiles", "Rubber and Leather"],
                        "Other_Organic":     ["Other_Organic"],
                        }
                return
#################################################################################################################

class Waste_Emissions_table(object):
    def __init__(self,):
        '''
        tCO2 / t waste
        '''
        self.waste_emission_table ={
                "Food":1.890 ,
                "Garden":1.480,
                "Wood":1.800,
                "Other_Organic":1.648,
                "Paper/Cardboard":2.940,
                "Inert":0.000,
                "Mixed MSW":1.640,
                "Other":1.500,
                "Textiles":1.420,
                "Rubber and Leather":2.940,
                }
        return
#################################################################################################################
if __name__ == "__main__":
    WCT = Waste_Composition_table()
    WET = Waste_Emissions_table()
    
    for waste_category in WCT.waste_comp:
        for index, waste_comp in enumerate(WCT.waste_comp[waste_category]):
                print("waste cat", waste_category, waste_comp, " emits ", WET.waste_emission_table[waste_comp], " tCO2 per t")
                