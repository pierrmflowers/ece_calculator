# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 11:02:39 2024

@author: bac0n
"""
#used for pi
import math as meth
#used for integrating indefinite integrals
import sympy as sy
#used for graphing
import matplotlib.pyplot as plt



#simple op amp eqautions:
#Inverting Op Amp Out = -(Vin * Rf/R1)
#Non-inverting Op Amp Out = Vin * ((Rf/R1) +1) 



#storage system

#storage_bin class will store basic values for comuptation (ie resistor values and constants)

class storage_bin():
    def __init__(self):
        #storage value for math
        index = 0
        self.resistor_values  = [0] * 168
        self.resistor_base = [1,1.1,1.2,1.3,1.5,1.6,1.8,2,2.2,2.4,2.7,3,3.3,3.6,3.9,4.3,4.7,5.1,5.6,6.2,6.8,7.5,8.2,9.1]
        for i in range(7):
            for j in range(24):
                self.resistor_values[index+j] = round(self.resistor_base[j] * (10**i), 3)
            #increments array indices
            index = index + j + 1
        #reset index for next loop
        index = 0
        #more or less true for our purposes
        self.capacitor_values = [0] * 288
        for i in range(12):
            for j in range(24):
                self.capacitor_values[index+j] = self.resistor_base[j] * (10**-i)
            #increments array indices
            index = index + j + 1
                
main_bin = storage_bin()
#for testing storage bin results
#test0= storage_bin()
#print(test1.resistor_values)






#function system:
    
#simple_op_amp_func will solve all 1 step op amp systems
#4 inputs: R1/C1, Rf/Cf, Vin, and Op_type

#resistor finder will find the minimum number of resistors to reach a target number
#this may/may not work as intended

#Vin, Val1, Val2, freq are all floating point ints
#op_type should be a string
#returns a floating point int
def simple_op_amp_func(Vin, Val1, Val2, Op_type):
    Vout = 0
    if (Op_type == 'inverting'):
        #Inverting Op Amp Out = -(Vin * Rf/R1)
        Vout = -(Vin * (Val2/Val1))
    elif (Op_type == 'non-inverting'):
        #Inverting Op Amp Out = -(Vin * Rf/R1)
        Vout = Vin * ((Val2/Val1) + 1)
    else:
        raise TypeError("Op-amp type was either not a string or was passed incorrectly")
    return Vout

def feedback_filtered(R1,fc):
    output = 1/(2 * meth.pi * fc * R1)
    return output

def resistor_finder(Freq, gain, circuit_type, input_voltage_eqaution):
    #output array for desired resistor pairs
    output_pairs = []
    #output array for graphing things
    output_array = []
    #calculate w
    w = 2 * meth.pi * Freq
    #option 1: inverting op amp
    #gain = RF/R1
    if circuit_type == 1:
        for i in range(168):
            for j in range(168):
                if round(main_bin.resistor_values[i]/main_bin.resistor_values[j], 4) == gain:
                    output_pairs.append(f"RF = {main_bin.resistor_values[i]}, R1 = {main_bin.resistor_values[j]}\n")
    
    #option 2 = non-inverting op-amp
    #gain = RF/R1 + 1
    elif circuit_type == 2:
        for i in range(168):
            for j in range(168):
                if round((main_bin.resistor_values[i]/main_bin.resistor_values[j]) + 1, 4) == gain:
                    output_pairs.append(f"RF = {main_bin.resistor_values[i]}, R1 = {main_bin.resistor_values[j]}\n")
                    
    #option 3 = inverting integrator
    #gain = (-1/RC)_/f(x) = (-1/(jwrc))(Vin) 
    #we're just solving for -1/R*C*w for now
    #w = 2 * pi * freq
    elif circuit_type == 3:
        for i in range(168):
            for j in range(240):
                if round(-1/(main_bin.resistor_values[i]*main_bin.capacitor_values[j]*w), 4) == gain:
                    output_pairs.append(f"R1 = {main_bin.resistor_values[i]}, CF = {main_bin.capacitor_values[j]}\n")
                    print(round(-1/(main_bin.resistor_values[i]*main_bin.capacitor_values[j]*w), 4))
                #output_array.append({{main_bin.capacitor_values[j]})
            #plt.plot(output_array)
            #plt.ylabel(f'Gain')
            #plt.xlabel(f'Capacitance')
            #plt.show()
            #output_array = []
    return output_pairs



#resistor finder test cases    
#val1 - frequency 
#val2 = gain desired
#val3 = circuit type
hw4 = resistor_finder(0,50,1,2)

#342 Lab 1 Stuff
output = resistor_finder(0,10,2,2)
feedback_resistors = []
feedback_capacitors = []
for result in output:
    feedback_resistors.append(float(result.split(",")[0].split(" ")[2]))

for resistor in feedback_resistors:
    print(feedback_filtered(resistor,10000))
    feedback_capacitors.append(feedback_filtered(resistor,10000))

    





