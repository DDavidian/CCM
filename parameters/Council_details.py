# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:07:10 2019

@author: Dee Davidian
"""

import numpy as np

class Council_info(object):
    def __init__(self,):

        self.Council_info = {
                "Council name" : "Metro"
                }
        self.housing_type_info = {
                "SUD" : {"Number of households" : 74675","Number of buildings" : 74675, "Number of bins" : 74 675},
                "MUD" : {"Number of households" : 74675","Number of buildings" : 74675, "Number of bins" : 74 675},
                         }
        self.waste_growth = {
                "Waste_Growth%" : 4.9},
                }
        self.pop_growth = {
                "Population_Growth%" : 4.9},
                }
        self.levy_system = {
                "Levy_System" : "VIC"},
                }
        self.region= {
                "region" : "metro"},
                }
        return
    
