# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:39:13 2019

@author: Dee Davidian
"""
try:
    from ..parameters import Waste_Facility as WF
    from ..parameters import Composition as Co
    from ..parameters import Ngers as Ng
except:
    import sys
    sys.path.append("../parameters")
    import Waste_Facility as WF
    import Composition as Co
    import Ngers as Ng
    
class Processing(object):

    def __init__(self,Processing_Facility, Total_tonnes_processed,gate_fee, Waste_Composition):
        self.Processing_Facility = WF.Processing_Facility
        self.Waste_stream = 0
        self.Total_processed_tonnes = Total_processed_tonnes
        self.Processing_Facility_class = WF.Facility_Type()
        self.waste_composition_class = Co.Composition(WasteStream)()
        self.Processing_Emissions_class = Ng.processing_emissions()
        self.tCO2 = self.emissions * self.Waste_Composition
        self.gate_fee= 0
        return
##############################################################
    def total_emissions(self,):
        self.total_emissions = self.tCO2_per_tonne * total_processed_tonnes
        return
    def costs(self,):
        self.gate_fee= self.Processing_Facility_class.Facility_Gate_Fee["GateFee($/tn"]
        self.total_processed_tonnes= Total_processed_tonnes
        print ("total processing cost=",self.gate_fee * total_processed_tonnes )
################################################################################################################
if __name__ == "__main__":
    Processing_Facility = WF.Processing_Facility()
    for Processing_Facility in WF.Facility_Type:
        Processing_Method = "MRF"
        GateFee = 95
        Material_Diversion = "MRF"
        Processing_Facility = "Manly_The Universe"

        WP = Processing(Processing_Facility, Total_tonnes_processed,gate_fee, Waste_Composition)
        WP.total_emissions()
        WP.costs()
        print ("total emissions in t CO2 = ", WP.total_emissions, " total processing cost = ", WP.costs)