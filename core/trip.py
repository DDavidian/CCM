# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:24:01 2019

@author: Dee Davidian
"""
from ..parameters import Fuel_emissions as FE

class Trip(object):
    '''
    truck_type: dict
    
    '''
    def __init__(self, ):
        self.truck_type =
        self.Distance_per_lift
        self.Distance_to_TransertStation
        self.Total_tonnes_collected
        self.Number_bin_per_hhold
        self.number_hhold
        self.Waste_stream
        self.Facility_Name
        self.Waste_Composition
        self.Lift_rate
        return
##############################################################
    def total_emissions(self,):
        self.Distance_per_run = self.number_hhold * self.Distance_per_lift + self.Distance_to_TransferStation
        