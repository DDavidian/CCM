# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:54:52 2019

@author: Dee Davidian
"""

class Fuel_Emissions (object):
    def __init__(self,):
        self.fuel_emissions = {
           "Diesel" : {"GJ/kL" : 38.6, "CO2": 69.2, "CH4": 0.1,"N2O": 0.2, "l/km": 0.4, "cost/l": 1.55},
#           "Diesel NC":,
#           "Petrol":,
#           "Biodiesel":,
#           "Ethanol":,
                }
        return
    def derivative_quantities(self, fueltype):
        '''
        t CO2-e/L = GJ/kl * SUM ( CO2, CH4,N2O)/1000/1000
        tCO2-e/km = t CO2-e/L*L/km
        '''
        self.tCO2_per_l = self.fuel_emissions[fueltype]["GJ/kL"] * \
                (self.fuel_emissions[fueltype]["CO2"] + \
                 self.fuel_emissions[fueltype]["CH4"] + \
                 self.fuel_emissions[fueltype]["N2O"]) * 1E-6
        self.tCO2_per_km = self.tCO2_per_l * self.fuel_emissions[fueltype]["l/km"]
        return

############################################################################################################################
if __name__ == "__main__":
    FE = Fuel_Emissions()
    fueltype = "Diesel"
    FE.derivative_quantities(fueltype)
    print(FE.tCO2_per_km)
    
#
#        self.Collection_Emissions = {
#                         "tCO2-e/km".........:{"Fuel_1":  ,"Fuel_2": , "Fuel_3" , "Fuel_4":  ,"Fuel_5":  }
#            """
#    t CO2-e/L*L/km)
#    """
#                         "$/km"..............:{"Fuel_1": ,"Fuel_2": , "Fuel_3" , "Fuel_4":  ,"Fuel_5":  }
#            """
#    L/km* cost/L
#    """
#                         "GJ/kL".............:{"Fuel_1": 38.6,"Fuel_2": 38.6, "Fuel_3": 38.8, "Fuel_4": 34.6,"Fuel_5": 23.4}
#            """
#    energy content factor
#    """
#                         "CO2"..... .........:{"Fuel_1": 69.2,"Fuel_2": 69.2, "Fuel_3": 27.9, "Fuel_4": 0,"Fuel_5": 0}
#            """
#    Emission factor (kg CO2-e/GJ)
#    """
#                         "CH4"...............:{"Fuel_1": 0.1,"Fuel_2": 0.1, "Fuel_3": 0, "Fuel_4": 0.06,"Fuel_5": 0.06}
#                         "N2O"...............:{"Fuel_1": 0.2,"Fuel_2": 0.2, "Fuel_3": 0, "Fuel_4": 0.2,"Fuel_5": 0.2}
#                         "t CO2-e/L".........:{"Fuel_1":  ,"Fuel_2": , "Fuel_3" , "Fuel_4":  ,"Fuel_5":  }
#            """
# GJ/kl * SUM ( CO2, CH4,N2O)/1000/1000
#    """
#                         "L/km"..............:{"Fuel_1": 0.4,"Fuel_2": 0.4, "Fuel_3": 0.4, "Fuel_4": 0.4,"Fuel_5": 0.4}
#                         "cost/L"............:{"Fuel_1": 1.55,"Fuel_2": 1.55, "Fuel_3": 1.55, "Fuel_4": 1.55,"Fuel_5": 1.55}
#            """
#    energy content factor
#    """
#    }
