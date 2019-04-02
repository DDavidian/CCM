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

        self.trucks = {
'Vehicle 1':{"Vehicle_Code": "GCV", "Description": "Collection_Garbage_Collection_Vehicle ",             "Capacity(t)" : 7.5,  "Fuel Type": "Diesel", "$/lift": 1.10, "Km travelled per lift": 0.03},
'Vehicle 2':{"Vehicle_Code": "RCV", "Description": "Collection_Comingled_Recycling_Collection_Vehicle",  "Capacity(t)" : 7.5,  "Fuel Type": "Diesel", "$/lift": 1.50, "Km travelled per lift": 0.04},
'Vehicle 3':{"Vehicle_Code": "OCV", "Description": "Collection_Organics_Collection_Vehicle",             "Capacity(t)" : 7.5,  "Fuel Type": "Diesel", "$/lift": 1.10, "Km travelled per lift": 0.02},
'Vehicle 4':{"Vehicle_Code": "RTV", "Description": "Transfer_Recycling_Transfer_Vehicle",                "Capacity(t)" : 30,   "Fuel Type": "Diesel",},		
'Vehicle 5':{"Vehicle_Code": "OTV", "Description": "Transfer_Organics_Transfer_Vehicle",                 "Capacity(t)" : 30,   "Fuel Type": "Diesel",},		
'Vehicle 6':{"Vehicle_Code": "GTV", "Description": "Transfer_Garbage_Transfer_Vehicle",                  "Capacity(t)" : 30,   "Fuel Type": "Diesel",},			
}
        return
    
####################################################################################################################################
if __name__== '__main__':
    TT = trucks()
    print(TT.trucks)       