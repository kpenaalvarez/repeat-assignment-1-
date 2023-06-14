# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:47:49 2023

@author: kpenaalvarez
"""


def calculate_max_height(v0, g):
    t = v0 / g  # time taken to reach max height
    h_max = (v0 * t) - (0.5 * g * t**2)  # max height formula
    return h_max

def main():
    v0 = float(input(" Enter the initial velocity of the ball (ft/sec): "))
    g = 32.8  # force of gravity in ft/sec^2
    
    h_max = calculate_max_height(v0, g)
    
    print(f" The max height reached by the ball is {h_max:.2f} ft.")
    
if __name__ =="__main__":
    main()