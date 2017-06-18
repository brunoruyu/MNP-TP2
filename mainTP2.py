# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 11:26:36 2017

@author: bruno
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import ReadTP2
import ProbDF
archivo="CustomerSample.dat"
G,L,E='Gaussian','Linear','Epa'


df,buenos,malos=ReadTP2.ReadCsv(archivo)
segur=np.array(buenos['Z'])
riesg=np.array(malos['Z'])
score=np.array(df['Z'])

minZ=score.min()
maxZ=score.max()

X=np.arange(minZ-50,maxZ+50,1)
h=1.06*score.std()*len(score)**(-1/5)

print(h)
f_tot=[ProbDF.PDF(x,score,G,h) for x in X] 
f_seg=[ProbDF.PDF(x,segur,G,h) for x in X] #Gaussian, Linear o Epa
f_riesg=[ProbDF.PDF(x,riesg,G,h) for x in X]
         
P_tot=[np.trapz(f_tot,x) for x in X]         
#P_tot=[np.trapz(f_tot,x) for x in X]         

print(P_tot)
         
#plt.plot(X,f_seg,label='Seguros')
#plt.plot(X,f_riesg,label='Riesgosos')

plt.plot(X,f_tot,label='Todos')
plt.legend(loc=0)

#from sklearn.neighbors.kde import KernelDensity
#X = np.array([[])
#kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
#kde.score_samples(X)


