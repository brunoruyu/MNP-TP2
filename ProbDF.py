# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:08:12 2017

@author: bruno
"""
import numpy as np
from itertools import tee, islice, chain

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
        #return max(3/4*(1-(u**2)),0)   
        return max(3/4*(1-(u**2)/5)/np.sqrt(5),0)   
    else:
        sys.exit('Elegir bien el Kernel')
    
        
def SeqInt(f,X):
    F=np.zeros(len(X))
    for i in range(0,len(X)):
        if i==0:
            F[i]=0
        else:
            F[i]=F[i-1]+(X[i]-X[i-1])*(f[i]+f[i-1])/2
    return F

#def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)
    