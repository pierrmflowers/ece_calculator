# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:24:48 2024

@author: bac0n
"""
import math

#Fourmula is Disspation * Xc
#Xc = 1/wc or 1/2*pi*f*c

#all of these values were obtained expierimentally during lab1
freq = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
capacitor_capacitance = [1.197,1.197,1.197,1.197,1.197,1.197,1.197,1.197,1.197,1.197]
capacitor_dissapation = [0.0001,0.00012,0.00014,0.00015,0.00013,0.00012,0.00011,0.0001,0.00009,0.00009]
#gator_capacitance = [104,103,103,103,103,103,103,103,102,102]
#gator_dissapation = [0.00817,0.00181,0.00148,0.00211,0.00143,0.00145,0.00147,0.00143,0.00143,0.000773]

def esr_calc(freq, capacitance, dissapation):
    output = [[0] * 10 for i in range(len(freq))]
    for i in range(len(freq)):
        #10^-12 accounts for the pF
        output[i] = dissapation[i] * (1/(2*math.pi*freq[i]*capacitance[i]*10**-9))
    print(output)

print("Probe ESR")
esr_calc(freq, capacitor_capacitance, capacitor_dissapation) 
#print("Gator ESR")   
#esr_calc(freq, gator_capacitance, gator_dissapation)    
        
    


