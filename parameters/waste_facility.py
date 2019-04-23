# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:43:31 2019

@author: Dee Davidian
"""


import numpy as np

class Waste_Facility(object):
    def __init__(self,):
                self.Facility_Name = {
        "Facility_1"              {"Landfill"}
        "Facility_2"              {"MRF"}
        "Facility_3"              {"GO"}
        "Facility_4"              {"FOGO"}
        "Facility_5"              {"WTE"}
                }
        self.Facility_Gate_Fee= 
        self.GateFee = {"GateFee($/tn)": {"Facility1": 64, "Facility2": 60, "Facility3": 65, "Facility4":90, "Facility5":150}
                }
        self.Processing_Method= 
        "Landfill"...............................:{"Facility_1"}
        "MRF"....................................:{"Facility_2"}
        "Open_Windrow_Composting"................:{"Facility_3"}
        "Enclosed_Composting"....................:{"Facility_4"}
        "EfW"....................................:{"Facility_5"}
        "AWT_aerobic"............................:{"Facility_6"}
        "AWT_anaerobic"..........................:{"Facility_7"}
        "Transfer_station".......................:{"Facility_8"}
        "Chipping_Service".......................:{"Facility_9"}
        "Aerated_Windrow_Composting".............:{"Facility_10"}
                }
            """
    Include residuals facility as part of any facility name and processing method
    """
        self.Gas_capture = {
        "0"
        "0-25%"
        "25-50%"
        "50-75%"
        "75-100%"
        "100%"
                }
        self.Material_Diversion = {
                "Residual":                {"Facilty_1": 0, "Facility_2": 0, "Facility_3": 0, "Facility_4": 0, "Facility_5": 97 },
                "FO":                      {"Facilty_1": 0, "Facility_2": 0, "Facility_3": 0, "Facility_4": 95, "Facility_5": 97 },
                "GO":                      {"Facilty_1": 0, "Facility_2": 0, "Facility_3": 98 , "Facility_4": 98, "Facility_5": 97 },
                "Other organic":           {"Facilty_1": 0, "Facility_2": 0, "Facility_3": 95 , "Facility_4": 98, "Facility_5": 97 },
                "Paper/Cardboard":         {"Facilty_1": 0, "Facility_2": 95, "Facility_3": 0, "Facility_4": 0, "Facility_5": 97 },
                "Plastic":                 {"Facilty_1": 0, "Facility_2": 95, "Facility_3": 0, "Facility_4": 0, "Facility_5": 97 },
                "Glass":                   {"Facilty_1": 0, "Facility_2": 95, "Facility_3": 0, "Facility_4": 0, "Facility_5": 97 },
                "Metal":                   {"Facilty_1": 0, "Facility_2": 95, "Facility_3": 0, "Facility_4": 0, "Facility_5": 97 },
                "Other":...................{"Facilty_1": 0, "Facility_2": 0, "Facility_3": 0, "Facility_4": 0, "Facility_5": 97 },
                }
        return
