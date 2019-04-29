# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:08:13 2019

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
    
class Transfer(object):
    '''
    truck_type: dict
    
    '''
    def __init__(self, truck_type, 
                 TransferStation, 
                 Processing_Facility, Transfer_Distance, Total_tonnes_collected):
        self.truck_type = truck_type
        self.Transfer_Distance = Transfer_Distance
        self.Waste_stream = 0
        self.Facility_Name = 0
        
        self.fuel_emission_class = FE.Fuel_Emissions()
        self.truck_class = TR.trucks() 
        
        self.fuel_type = self.truck_class.transfer_trucks[self.truck_type]["Fuel_Type"]
        self.fuel_emission_class.derivative_quantities(self.fuel_type)
        self.tCO2_per_km = self.fuel_emission_class.tCO2_per_km
        print (self.fuel_type, self.tCO2_per_km)
        return
##############################################################
    def total_emissions(self,):
        self.Distance_per_run = self.Transfer_Distance
        print (self.fuel_type, self.tCO2_per_km)
        self.tCO2 = self.Transfer_Distance * self.tCO2_per_km
        return
    def costs(self,):
        self.transfer_costs = 0
################################################################################################################
if __name__ == "__main__":
    Trucks = TR.trucks()
    for transfer_truck in Trucks.transfer_trucks:
        Transfer_Distance = 5 
        Total_tonnes_transferred = 1
        Transfer_Station = "ManlyDam"
        Processing_Facility = "The Universe"

        TT = Transfer(transfer_truck, 
                 Transfer_Station, 
                 Processing_Facility, Transfer_Distance, Total_tonnes_collected)
        TT.total_emissions()
        TT.costs()
        print ("total emissions in t CO2 = ", TT.tCO2, " total transfercost = ", TT.transfer_costs)
    