# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:43:31 2019

@author: Dee Davidian
"""


import numpy as np

class Facility_Type(object):
    def __init__(self,):
                self.Processing_Method = {
        "Landfill":  ["Landfill"],
        "MRF":       ["MRF"],
        "GO":        ["Open_Windrow_Composting","Enclosed_Composting","Aerated_Windrow_Composting","AWT_aerobic","AWT_anaerobic"],
        "FOGO":      ["Open_Windrow_Composting","Enclosed_Composting","Aerated_Windrow_Composting","AWT_aerobic","AWT_anaerobic"],
        "WTE":       ["EfW"],
                }
                self.Facility_Gate_Fee= 
                self.GateFee = {"GateFee($/tn)": {"Facility1": 64, "Facility2": 60, "Facility3": 65, "Facility4":90, "Facility5":150}
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
                "Landfill":        ["Residual":0  , "FO":0  ,"GO":0  ,"Other organic":0  ,"Paper/Cardboard":0  ,"Plastic":0  ,"Glass":0  ,"Metal":0  ,"Other":0  ],
                "MRF":             ["Residual":0  , "FO":0  ,"GO":0  ,"Other organic":0  ,"Paper/Cardboard":95  ,"Plastic":95  ,"Glass":95  ,"Metal":95  ,"Other":0  ],
                "GO":              ["Residual":0  , "FO":0  ,"GO":98  ,"Other organic":95  ,"Paper/Cardboard":0  ,"Plastic":0  ,"Glass":0  ,"Metal":0  ,"Other":0  ],
                "FOGO":            ["Residual":0  , "FO":0  ,"GO":98  ,"Other organic":98  ,"Paper/Cardboard":0  ,"Plastic":0  ,"Glass":0  ,"Metal":0  ,"Other":0  ],
                "WTE":             ["Residual":97  , "FO":0  ,"GO":97  ,"Other organic":97  ,"Paper/Cardboard":97  ,"Plastic":97  ,"Glass":97  ,"Metal":97  ,"Other":97  ],
                }

        return
