# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
from matplotlib import pyplot as plt 

def gaussian(x,mu,sig):
    r = np.exp(-(x-mu)**2/2/sig**2)
    return r

# x=np.linspace(0,20,300)
# y=np.zeros_like(x)

# for i in range(len(x)):
#     y[i]=gaussian(x[i],5,1)
    
# plt.figure(0)
# plt.plot(x,y)
# plt.show()

#Increasing function
def inc(x, a, b):
    if x<a:
        r=0
    elif x>b:
        r=1
    else:
        r=(x-a)/(b-a)
    return(r)


#Decreasing function 
def dec(x, a, b):
    if x<a:
        r=1
    elif x>b:
        r=0
    else:
        r=(b-x)/(b-a)
    return(r)

#Trapezoidal function 
#lazy method 
#r1 = inc(x, a, b)
#r2 = dec(x, a, b)
#r = r1 + r2

#trap math method 
def trap(x,a,b,c,d):
    
    if x<a or x>d:
        r = 0
    elif x>=b and x<=c:
        r = 1
    elif x>=a and x<=b:
        r = (x-a)/(b-a)
    else:
        r = (d-x)/(d-c)
    return(r)
# x=np.linspace(0,20,300)
# y=np.zeros_like(x)

# for i in range(len(x)):
#     # y[i]=gaussian(x[i],5,1)
#     y[i]=trap(x[i],5,10,12,15)
    
# plt.figure(0)
# plt.plot(x,y)
# plt.show()

#Sigmoid 
def sig_bad(x):
    r=1/(1+np.exp(-x))
    return(r)


# x=np.linspace(-10,10,300)
# y=np.zeros_like(x)
# for i in range(len(x)):
#     y[i]=sig(x[i])

# plt.figure("Sigmoid")
# plt.plot(x,y)
# plt.xlabel("X")
# plt.ylabel("Membership")
# plt.show()

#Sigmoid membership function
# +ve a is increasing, -ve a is decreasing. Larger a is sharp and Smaller a is smooth. b determines the center of the sigmoid function  
def sig(x,a,b):
    r=1/(1+np.exp(-a*(x-b)))
    return(r)


x=np.linspace(-30,50,200)
y=np.zeros_like(x)
y1=np.zeros_like(x)
for i in range(len(x)):
    y[i]=sig(x[i],1,-3)
    # y1[i] = sig(x[i], 0.7, 0)

plt.figure("Sigmoid")
plt.plot(x,y)
# plt.plot(x,y1,color=(1,0,0))
plt.xlabel("X")
plt.ylabel("Membership")
plt.show()


