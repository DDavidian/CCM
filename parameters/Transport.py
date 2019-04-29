# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:17:42 2019

@author: Dee Davidian
"""

class trucks(object):
    """
    class to define dictionary of trucks
    """
    def __init__(self,):

        self.collection_trucks = {
'GCV':{ "Description": "Collection_Garbage_Collection_Vehicle ",             "Capacity(t)" : 7.5,  "Fuel_Type": "Diesel", "$/lift": 1.10, "Km_per_lift": 0.03},
'RCV':{ "Description": "Collection_Comingled_Recycling_Collection_Vehicle",  "Capacity(t)" : 7.5,  "Fuel_Type": "Diesel", "$/lift": 1.50, "Km_per_lift": 0.04},
'OCV':{ "Description": "Collection_Organics_Collection_Vehicle",             "Capacity(t)" : 7.5,  "Fuel_Type": "Diesel", "$/lift": 1.10, "Km_per_lift": 0.02},
}
        
        self.transfer_trucks = {
'RTV':{ "Description": "Transfer_Recycling_Transfer_Vehicle",                "Capacity(t)" : 30,   "Fuel_Type": "Diesel",},
'OTV':{ "Description": "Transfer_Organics_Transfer_Vehicle",                 "Capacity(t)" : 30,   "Fuel_Type": "Diesel",},
'GTV':{ "Description": "Transfer_Garbage_Transfer_Vehicle",                  "Capacity(t)" : 30,   "Fuel_Type": "Diesel",},
}
        
        return
    
####################################################################################################################################
if __name__== '__main__':
    TT = trucks()
    print(TT.collection_trucks)       