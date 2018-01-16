# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:03:24 2018

@author: Gavrilov
"""

#Numerical Stability
x = 1000000000
for i in range(1000000):
    x+=1e-6 #0.000001
x-=1000000000
print(x)
#it must be 1.0, but result is around 0.953    