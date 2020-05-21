# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:10:18 2020

@author: diama
"""
import trip as Trp
import transfer as Trf
import processing as Prcss
import wastestream as wststream

try:
    from ..parameters import waste_facility as WF
    from ..parameters import Composition as Co
    from ..parameters import Ngers as Ng
    from ..parameters import Fuel_emissions as FE
    from ..parameters import Transport as TR
    
except:
    import sys
    sys.path.append("../parameters")
    import waste_facility as WF
    import Composition as Co
    import Ngers as Ng
    import Fuel_emissions as FE
    import Transport as TR

class ProcessScenario(object):

    def __init__(self, 
                 Facility_Name, facility_type,
                 Distance_per_lift, Distance_to_TransferStation, 
                 Total_tonnes_collected, Number_bin_per_hhold, number_hhold, 
                 Transfer_Station, 
                 Processing_Facility, Transfer_Distance, 
                 ):

        self.Facility_Name = Facility_Name
        self.facility_type = facility_type
        self.Distance_per_lift = Distance_per_lift
        self.Distance_to_TransferStation = Distance_to_TransferStation
        self.Total_tonnes_collected = Total_tonnes_collected
        self.Number_bin_per_hhold = Number_bin_per_hhold
        self.number_hhold = number_hhold
        self.Transfer_Station = Transfer_Station
        self.Processing_Facility = Processing_Facility
        self.Transfer_Distance = Transfer_Distance
        
        ###########################################################################################################
        #processing facility
        
        #grab composition
        self.waste_composition_class = Co.Waste_Composition()
        #grab mat diversion per facility
        self.Material_Diversion_class = WF.Facility_Type()
        
        self.WP = Prcss.Processing(self.Facility_Name, self.waste_composition_class, self.Material_Diversion_class)
        self.WP.Material_Recovery(facility_type)
        
        self.total_landfill_in_t = self.WP.total_for_landfill
        self.total_processed = self.WP.total_processed
        print ("total landfill in t = ", self.WP.total_for_landfill, " total processed = ", self.WP.total_processed)        
        
        ###########################################################################################################
        #waste stream
        self.WasteCompo = self.waste_composition_class.Waste_Composition
        self.WS = wststream.WasteStream(self.WasteCompo)

        #self.WS.verification()
        for compo in self.WS.Waste_Composition:
            self.WS.landfill_emissions_per_t(compo)
            print(compo, " total emissions per t = ", self.WS.total_emission_per_t)    

        ###########################################################################################################
        #trip from households to transfer station
        self.Trucks = TR.trucks()
        for collection_truck in self.Trucks.collection_trucks:
            self.TRP = Trp.Trip(collection_truck, 
                 self.Distance_per_lift, self.Distance_to_TransferStation, 
                 self.Total_tonnes_collected, self.Number_bin_per_hhold, self.number_hhold)
            self.TRP.total_emissions()
            self.TRP.costs()
            print ("Collection truck = ", collection_truck, " total emissions in t CO2 = ", self.TRP.tCO2, " total liftcost = ", self.TRP.lift_costs)
        
        ###########################################################################################################
        #transfert from transfert station to processing facility
        for transfer_truck in self.Trucks.transfer_trucks:
            self.TRANS = Trf.Transfer(transfer_truck, 
                                     self.Transfer_Station, 
                                     self.Processing_Facility, self.Transfer_Distance, self.Total_tonnes_collected)
            self.TRANS.total_emissions()
            self.TRANS.costs()
            print ("transfer truck = ", transfer_truck, " total emissions in t CO2 = ", self.TRANS.tCO2, " total transfercost = ", self.TRANS.transfer_costs)

        return
    
####################################################################################################################################
if __name__== '__main__':

    Material_Diversion = "MRF"

    Facility_Name = "Veolia"
    facility_type = "WTE"
    Distance_per_lift= 1
    Distance_to_TransferStation = 30
    Total_tonnes_collected = 1000
    Number_bin_per_hhold = 2
    number_hhold = 565000
        
    Transfer_Distance = 5 
    Total_tonnes_transferred = 1
    Transfer_Station = "ManlyDam"
    Processing_Facility = "The Universe"


    PS = ProcessScenario(
                 Facility_Name, facility_type,
                 Distance_per_lift, Distance_to_TransferStation, 
                 Total_tonnes_collected, Number_bin_per_hhold, number_hhold, 
                 Transfer_Station, 
                 Processing_Facility, Transfer_Distance, 
                 )