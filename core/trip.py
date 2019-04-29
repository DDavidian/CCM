# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:24:01 2019

@author: Dee Davidian
"""
try:
    from ..parameters import Fuel_emissions as FE
    from ..parameters import Transport as TR
except:
    import sys
    sys.path.append("../parameters")
    import Fuel_emissions as FE
    import Transport as TR
    
class Trip(object):
    '''
    truck_type: dict
    
    '''
    def __init__(self, truck_type, 
                 Distance_per_lift, Distance_to_TransferStation, 
                 Total_tonnes_collected, Number_bin_per_hhold, number_hhold):
        self.truck_type = truck_type
        self.Distance_per_lift= Distance_per_lift
        self.Distance_to_TransferStation = Distance_to_TransferStation
        self.Total_tonnes_collected = Total_tonnes_collected
        self.Number_bin_per_hhold = Number_bin_per_hhold
        self.number_hhold = number_hhold
        self.Waste_stream = 0
        self.Facility_Name = 0
        self.Waste_Composition = 0
        self.Lift_rate = 0
        
        self.fuel_emission_class = FE.Fuel_Emissions()
        self.truck_class = TR.trucks() 
        
        self.fuel_type = self.truck_class.collection_trucks[self.truck_type]["Fuel_Type"]
        self.fuel_emission_class.derivative_quantities(self.fuel_type)
        self.tCO2_per_km = self.fuel_emission_class.tCO2_per_km
        print (self.fuel_type, self.tCO2_per_km)
        return
##############################################################
    def total_emissions(self,):
        self.Distance_per_run = self.number_hhold * self.Distance_per_lift + self.Distance_to_TransferStation
        print (self.fuel_type, self.tCO2_per_km)
        self.tCO2 = self.Distance_per_run * self.tCO2_per_km
        return
    def costs(self,):
        costperlift = self.truck_class.collection_trucks[self.truck_type]["$/lift"]
        self.lift_costs = self.number_hhold * self.Number_bin_per_hhold * costperlift
################################################################################################################
if __name__ == "__main__":
    Trucks = TR.trucks()
    for collection_truck in Trucks.collection_trucks:
        Distance_per_lift= 1
        Distance_to_TransferStation = 30
        Total_tonnes_collected = 1
        Number_bin_per_hhold = 3
        number_hhold = 1000
        
        TT = Trip(collection_truck, 
                 Distance_per_lift, Distance_to_TransferStation, 
                 Total_tonnes_collected, Number_bin_per_hhold, number_hhold)
        TT.total_emissions()
        TT.costs()
        print ("total emissions in t CO2 = ", TT.tCO2, " total liftcost = ", TT.lift_costs)
    