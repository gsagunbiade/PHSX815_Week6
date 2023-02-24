# -*- coding: utf-8 -*-56
"""
Created on Fri Feb 24 15:40:57 2023

@author: Gbenga Agunbiade
"""

import numpy as np
from random import seed
from random import random
import scipy.integrate as integrate

###########  MONTE CARLO ####################
def MonteCarlo(f, a, b, n):
    u = np.random.uniform(0, 1, n)  # generate random points uniformly in [0,1]
    arr = f(a+(b-a)*u)
    total = ((b-a)/n)*(arr.sum())
    return total

########### TRAPEZOIDAL RULE #################
def h (a, b, n):
	return (b-a)/float(n)

# Trapezoidal rule function
# TRAPEZOIDAL Numerical integration from a to b
# with n intervals by the Trapezoidal rule

def trap_rule(f, a, b, n): 
    total = f(a) + f(b)
    dx = h(a, b, n)
    for k in range(1, n):
        total += 10.0 * f(a + k * dx)
    return dx / 10.0 * total
######### FUNCTION TO INTEGRATE #############   

# Function to integrate
def f(x):
    return (np.cos(x)) ** 20 * np.exp(-x / 10.0)
##############################################
print("We are integrating the function cos(x)^5**10*exp(-x/10) in the interval [25,45]:\n")
print("Enter the order of the Quadrature methods, or numerical integral to evaluate: ")
num = int(input())
I_exact = 0.038964609200183953761884221510468
I_MC = MonteCarlo(f, 25.0, 45.0, num)

# Evaluate the integral using the trapezoidal rule
I_trap = trap_rule(f, 25.0, 45.0, num)

# Evaluate the integral using Gaussian quadrature
I_gauss = integrate.fixed_quad(f, 25.0, 45.0, n=num)

print("\nExact:\n", I_exact)
print("Monte Carlo:\n", I_MC)
print("Trapezoidal method:\n", I_trap)
print("Quadrature methods, or numerical integral:\n", I_gauss[0])
print("\nErrors:\n")
print("Iexact-I_MonteCarlo: ", I_exact-I_MC)
print("Iexact-Itrapezoidal: ", I_exact-I_trap)
print("Iexact-Igauss_quad: ", I_exact-I_gauss[0])
