# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:39:13 2019

@author: Dee Davidian
"""
try:
    from ..parameters import waste_facility as WF
    from ..parameters import Composition as Co
    from ..parameters import Ngers as Ng
except:
    import sys
    sys.path.append("../parameters")
    import waste_facility as WF
    import Composition as Co
    import Ngers as Ng
    
class Processing(object):

    def __init__(self, Facility_Name, waste_composition_class, Material_Diversion_class):
        self.Facility_Name = Facility_Name
        
        self.gate_fee= 0
        #grab composition
        self.waste_composition_class = waste_composition_class
        #grab mat diversion per facility
        self.Material_Diversion_class = Material_Diversion_class
        self.mat_diversion = self.Material_Diversion_class.Material_Diversion
        return
##############################################################
    def Material_Recovery(self, facility_type):
        
        residuals = 0.
        processed = 0.
        for wc, mattype in self.waste_composition_class.Waste_Composition.items():
            for mt, Waste_Composition in mattype.items(): 
                total_processed_per_type = self.waste_composition_class.Total_Tonnes_Received[wc] * Waste_Composition
                percent_processed = self.mat_diversion[facility_type][mt] * 0.01
                percent_not_processed = 1.- percent_processed
                
                residuals = residuals + total_processed_per_type * percent_not_processed
                processed = processed + total_processed_per_type * percent_processed
        self.total_for_landfill = residuals
        self.total_processed = processed
        return

##############################################################
    def total_emissions(self,):
        
        self.total_emissions= self.tonnes_recovered * (WF.Facility_Type_class.Processing_Method ["Indirect_upstream_emissions"]+WF.Facility_Type_class.Processing_Method ["Direct_process_emissions"])
        return
    def costs(self,):
        self.total_costs= self.Total_Tonnes_Received * self.gate_fee
        print ("total processing cost=",self.gate_fee * total_processed_tonnes )
################################################################################################################
if __name__ == "__main__":
        Material_Diversion = "MRF"
        Facility_Name = "Veolia"
        
        #grab composition
        waste_composition_class = Co.Waste_Composition()
        #grab mat diversion per facility
        Material_Diversion_class = WF.Facility_Type()

        facility_type = "WTE"
        WP = Processing(Facility_Name, waste_composition_class, Material_Diversion_class)
        WP.Material_Recovery(facility_type)
        print ("total landfill in t = ", WP.total_for_landfill, " total processed = ", WP.total_processed)