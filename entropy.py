#!/usr/bin/python3

"""
@author: Timothy Baker

entropy.py

"""

import math


entropy_dict = {'A': [0.5, 0, 0, 0.5], 'B': [0.25, 0.25, 0.25, 0.25],
'C': [0, 0, 0, 1], 'D': [0.25, 0, 0.5, 0.25]}

calc_dict = {}

def calculate_entropy(prob_dict):
    """ returns a sorted list of entropy values from low to high """

    for key, values in prob_dict.items():
        calc_dict[key] = math.log2(values)

    return calc_dict

print(calculate_entropy(entropy_dict))
