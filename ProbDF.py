# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:08:12 2017

@author: bruno
"""
import numpy as np

def PDF(x,score,tipo,h):
    n=len(score)
    pdf=0
    for z in score:
        pdf+=Kernel((x-z)/h,tipo)/(n*h)
    return pdf
    
def Kernel(u,tipo):
    if tipo=='Gaussian':
        return np.exp(-u**2/2)/np.sqrt(2*np.pi)
    elif tipo=='Linear':
        return max(1-np.abs(u),0)    
    elif tipo=='Epa':
        return max(3*(1-u**2)/4,0)   
    else:
        sys.exit('Elegir bien el Kernel')
    
        
def SeqInt(f,X):
    