from __future__ import division  
 
# Bissecção
def bissecao(f, a, b, TOL, N):  
    i = 1  
    fa = f(a)  
    while (i <= N):  
        #iteracao da bissecao  
        p = a + (b-a)/2  
        fp = f(p)  
        #condicao de parada  
        if ((fp == 0) or ((b-a)/2 < TOL)):  
            return p  
        #bissecta o intervalo  
        i = i+1  
        if (fa * fp > 0):  
            a = p  
            fa = fp  
        else:  
            b = p  
 
    raise NameError(’Num. max. de iter. excedido!’);

# Newton
def F(x):  
    y = np.zeros(2)  
 
    y[0] = x[0]**2 - np.cos(x[0]*x[1]) - 1  
    y[1] = np.sin(x[1]) - 2*np.cos(x[0])  
 
    return y  
 
def JF(x):  
    y = np.zeros((2,2))  
 
    y[0,0] = 2*x[0] + x[1]*np.sin(x[0]*x[1])  
    y[0,1] = x[0]*np.sin(x[0]*x[1])  
 
    y[1,0] =  2*np.sin(x[0])  
    y[1,1] = np.cos(x[1])  
 
    return y

from __future__ import division  
import numpy as np  
from numpy import linalg  
 
def newton(F,JF,x0,TOL,N):  
    #preliminares  
    x = np.copy(x0).astype(’double’)  
    k=0  
    #iteracoes  
    while (k < N):  
       k += 1  
       #iteracao Newton  
       delta = -np.linalg.inv(JF(x)).dot(F(x))  
       x = x + delta  
       #criterio de parada  
       if (np.linalg.norm(delta,np.inf) < TOL):  
           return x  
 
    raise NameError(’num. max. iter. excedido.’)