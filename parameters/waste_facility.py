# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:43:31 2019

@author: Dee Davidian
"""


import numpy as np

class Facility_Type(object):
       def __init__(self,):
           self.Processing_Method = {
       "Garden_Open_Windrow"       :           {"Facility_Type": "Open_Windrow_Composting",    "Indirect_upstream_emissions": 0.008100, "Direct_process_emissions": 0.048000},
       "Food&Garden_Open_Windrow"  :           {"Facility_Type": "Open_Windrow_Composting",    "Indirect_upstream_emissions": 0.08100,  "Direct_process_emissions": 0.048000},
       "Garden_enclosed"           :           {"Facility_Type": "Enclosed_Composting",        "Indirect_upstream_emissions": 0.000540, "Direct_process_emissions": 0.047930},
       "Food&Garden_enclosed"      :           {"Facility_Type": "Enclosed_Composting",        "Indirect_upstream_emissions": 0.000600, "Direct_process_emissions": 0.047930},
       "Garbage_AWT_aerobic"       :           {"Facility_Type": "AWT_aerobic",                "Indirect_upstream_emissions": 0.036000, "Direct_process_emissions": 0.042000},
       "Garbage_AWT_anaerobic"     :           {"Facility_Type": "AWT_aerobic",                "Indirect_upstream_emissions": 0.036000, "Direct_process_emissions": 0.042000},
       "Food_AD"                   :           {"Facility_Type": "Anaerobic_Digestor",         "Indirect_upstream_emissions": 0.025000, "Direct_process_emissions": 0.},
       "Comingled_MRF"             :           {"Facility_Type": "MRF",                        "Indirect_upstream_emissions": 0.036000, "Direct_process_emissions": 0.},
       "Containers_MRF"            :           {"Facility_Type": "MRF",                        "Indirect_upstream_emissions": 0.036000, "Direct_process_emissions": 0.},
       "Paper/Cardboard_MRF"       :           {"Facility_Type": "MRF",                        "Indirect_upstream_emissions": 0.036000, "Direct_process_emissions": 0.},
       "Garden_Chipping"           :           {"Facility_Type": "Chipping_Service",           "Indirect_upstream_emissions": 0.     ,  "Direct_process_emissions": 0.},
       "Garbage EfW"               :           {"Facility_Type": "EfW",                        "Indirect_upstream_emissions": 0.021960, "Direct_process_emissions": 0.},
       "Garden Aerated Windrow"    :           {"Facility_Type": "Aerated_Windrow_Composting", "Indirect_upstream_emissions": 0.000540, "Direct_process_emissions": 0.047930},
       "Food & Garden Aerated Windrow":        {"Facility_Type": "Aerated_Windrow_Composting", "Indirect_upstream_emissions": 0.000600, "Direct_process_emissions": 0.047930},
                                               }
           self.Material_Diversion = {
                "Landfill"    :    {"Residual":0.,  "FO":0, "GO":0.,   "Other_Organic":0.,      "Paper/Cardboard":0.,   "Plastic":0.   ,"Glass":0.   ,"Metal":0.,   "Other":0.  },
                "MRF"         :    {"Residual":0.,  "FO":0, "GO":0.,   "Other_Organic":0.,      "Paper/Cardboard":95.,  "Plastic":95.  ,"Glass":95.  ,"Metal":95.,  "Other":0.  },
                "GO"          :    {"Residual":0.,  "FO":0, "GO":98.,  "Other_Organic":95.,     "Paper/Cardboard":0.,   "Plastic":0.   ,"Glass":0.   ,"Metal":0.,   "Other":0.  },
                "FOGO"        :    {"Residual":0.,  "FO":0, "GO":98.,  "Other_Organic":98.,     "Paper/Cardboard":0.,   "Plastic":0.   ,"Glass":0.   ,"Metal":0.,   "Other":0.  },
                "WTE"         :    {"Residual":97., "FO":0, "GO":97.,  "Other_Organic":97.,     "Paper/Cardboard":97.,  "Plastic":97.  ,"Glass":97.  ,"Metal":97.,  "Other":97. },
                                    }
 

############################################################################################################################
#if __name__ == "__main__":
#    FE = Fuel_Emissions()
#    for fueltype in FE.fuel_emissions: 
#        FE.derivative_quantities(fueltype)
#        print(fueltype, FE.tCO2_per_km,FE.tCO2_per_l)#.tCO2_per_km)
#    
#
##(t CO2-e/t
#
#
#                self.Facility_Gate_Fee= 
#                self.GateFee = {"GateFee($/tn)": {"Facility1": 64, "Facility2": 60, "Facility3": 65, "Facility4":90, "Facility5":150}
#                }
#
#            """
#    Include residuals facility as part of any facility name and processing method
#    """
#        self.Gas_capture = {
#        "0"
#        "0-25%"
#        "25-50%"
#        "50-75%"
#        "75-100%"
#        "100%"
#                }


