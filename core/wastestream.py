# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:19:19 2019

@author: Dee Davidian
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:09:14 2019

@author: Dee Davidian
"""
import numpy as np
try:
    from ..parameters import Ngers
except:
    import sys
    sys.path.append("../parameters")
    import Ngers
    
class WasteStream(object):
    def __init__(self, Waste_Composition):
        self.Waste_Composition = Waste_Composition
        return
    def verification(self):
        for wc in self.Waste_Composition:
            total = [self.Waste_Composition[wc][typetype] for typetype in self.Waste_Composition[wc]]
            test = np.sum(total) #== 100
            print("test ", wc, " sum=100", test)
        return
    def landfill_emissions_per_t(self, wc):
        WCT = Ngers.Waste_Composition_table()
        WET = Ngers.Waste_Emissions_table()
        
        self.total_emission_per_t = 0.
        for waste_category in self.Waste_Composition[wc]:
            total_emission_per_cat = 0.
            for index, waste_comp in enumerate(WCT.waste_comp[waste_category]):
                #print("waste cat", waste_category, waste_comp, " emits ", WET.waste_emission_table[waste_comp], " tCO2 per t")
                total_emission_per_cat += WET.waste_emission_table[waste_comp]
            self.total_emission_per_t += self.Waste_Composition[wc][waste_category] * total_emission_per_cat * 0.01
        #print("total emissions per t = ", self.total_emission_per_t)    
        return

####################################################################################################################################
if __name__== '__main__':
    import Composition as CP
    WC = CP.WasteComposition()
    Waste_Composition = WC.Waste_Composition
    TT = WasteStream(Waste_Composition)
    TT.verification()
    for compo in TT.Waste_Composition:
        TT.landfill_emissions_per_t(compo)
        print(compo, " total emissions per t = ", TT.total_emission_per_t)    
