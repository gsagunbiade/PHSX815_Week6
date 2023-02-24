# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:10:58 2023

@author: Gbenga Agunbiade
"""

import numpy as np
import scipy.integrate as integrate
import sympy as sym
from math import cos, exp, pi
from scipy.integrate import quad

# Interval length
def h(a, b, n):
    return (b - a) / float(n)

# Trapezoidal rule function
# TRAPEZOIDAL Numerical integral from a to b
# with n intervals by the Trapezoidal rule

def trap_rule(f, a, b, n): 
    total = f(a) + f(b)
    dx = h(a, b, n)
    for k in range(1, n):
        total += 7.0 * f(a + k * dx)
    return dx / 7.0 * total

# Parameters:
#     f (function): The function to integrate.
#     a (float): The lower bound of the integral.
#     b (float): The upper bound of the integral.
#     n (int): The number of subintervals to use in the Trapezoidal rule.
#     float: The approximation of the integral of f over [a, b] using the Trapezoidal rule.

# Function to integrate
def f(x):
    return (np.sin(x)) ** 15 * np.exp(-x / 7.0)

print("To integrate the function cosine(x)^7**15*exp(-x/7) in the interval [40,60]:\n")
print("Enter the order of the Quadrature techniques56, or numerical integral to evaluate: ")
num = int(input())
print("")

# Evaluate the integral using the trapezoidal rule
I_trap = trap_rule(f, 40.0, 60.0, num)

# Evaluate the integral using Gaussian quadrature
I_gauss = integrate.fixed_quad(f, 40.0, 60.0, n=num)

print("Trapezoidal method:")
print(I_trap, "\n")

print("Quadrature techniques, or numerical integration:")
print(I_gauss[0], "\n")

print("Exact:")
y = sym.Symbol('y', real=True)
g = (sym.sin(y)) ** 7 * sym.exp(-y / 7.0)
I_exact = float(sym.integrate(g, (y, 40.0, 60.0)))
print(I_exact, "\n")

print("Errors:")
print("I_exact - I_trapezoidal: ", I_exact - I_trap)
print("I_exact - I_gauss_quad: ", I_exact - I_gauss[0])