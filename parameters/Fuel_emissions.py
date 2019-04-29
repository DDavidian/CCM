# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:54:52 2019

@author: Dee Davidian
"""

class Fuel_Emissions (object):
    def __init__(self,):
        self.fuel_emissions = {
           "Diesel" : {"GJ/kL" : 38.6, "CO2": 69.2, "CH4": 0.1,"N2O": 0.2, "l/km": 0.4, "cost/l": 1.55},
           "Diesel NC":{"GJ/kL" : 38.6, "CO2": 69.2, "CH4": 0.1,"N2O": 0.2, "l/km": 0.4, "cost/l": 1.55},
           "Petrol":{"GJ/kL" : 38.6, "CO2": 27.9, "CH4": 0.0,"N2O": 0.0, "l/km": 0.4, "cost/l": 1.55},
           "Biodiesel":{"GJ/kL" : 34.6, "CO2": 0.0, "CH4": 0.06,"N2O": 0.2, "l/km": 0.4, "cost/l": 1.55},
           "Ethanol":{"GJ/kL" : 23.4, "CO2": 0.0, "CH4": 0.06,"N2O": 0.2, "l/km": 0.4, "cost/l": 1.55},
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
    for fueltype in FE.fuel_emissions: 
        FE.derivative_quantities(fueltype)
        print(fueltype, FE.tCO2_per_km,FE.tCO2_per_l)#.tCO2_per_km)
    
