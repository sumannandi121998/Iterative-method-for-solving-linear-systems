#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:56:57 2020

@author: suman
"""

import numpy as np

A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=np.array([1,2,3,4,5])
L=np.tril(A,k=0) #This matrix contains the upper triangular elements of A
U=np.triu(A,k=1) #This matrix contains the lower triangular elements of A
l=np.linalg.inv(L) #inverse of matrix L
x=np.array([0,0,0,0,0]) #initial guess of solution
s=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163]) #true solution vector
j=0
while (any(np.abs(s[i]-x[i])>=0.01 for i in range (5))):
    x=np.dot(l,(b-np.dot(U,x)))
    j=j+1 #this denotes the no of iteration
print("The solution vector is",x) #print solution
print("The no of iteration to reach the accuracy is",j) #print the no of iteration 
