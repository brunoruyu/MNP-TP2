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
alfa=0.015
N=700

df,buenos,malos=ReadTP2.ReadCsv(archivo)
segur=np.array(buenos['Z'])
riesg=np.array(malos['Z'])
todos=np.array(df['Z'])

minZ=todos.min()
maxZ=todos.max()

dx=0.05
X=np.arange(minZ-2,maxZ+2,dx)

file_write = open('ResultadosTP2.dat', 'w')    
hopt=1.06*todos.std()*len(todos)**(-1/5)
hh=[0.05,0.1,0.25,0.5,1,1.5,2,3]
#hh=[1]
for ke in [L,G,E]:#[L,G,E]:
    for h in hh:
        #h=
        #ke=L   
        print('h=',h,'Kernel=',ke)
        
        f_tot=[ProbDF.PDF(x,todos,ke,h) for x in X] 
        f_seg=[ProbDF.PDF(x,segur,ke,h) for x in X] #Gaussian, Linear o Epa
        f_riesg=[ProbDF.PDF(x,riesg,ke,h) for x in X]
                 
        P_tot=np.trapz(f_tot,X) 
        #P_tot=[np.trapz(f_tot,x) for x in X]         
        F_tot=ProbDF.SeqInt(f_tot,X)
        F_seg=ProbDF.SeqInt(f_seg,X)
        F_riesg=ProbDF.SeqInt(f_riesg,X)
        
        cociente=F_riesg/F_tot
        z1=np.argmax(cociente>6*alfa)-1
        
        maxim=700*5/6*(F_seg-2*F_riesg)       
        z2=np.argmax(maxim)
        KS=max(np.abs(F_seg-F_riesg))
        print('z1=',X[z1])
        print('z2=',X[z2])
        
        string = ke+' '+str(h)+' '+str(X[z1])+' '+str(X[z2])+' '+str(KS)+ "\n"
        #print(string)
        file_write.write(string)
        
        #print(F_seg-F_riesg)
file_write.close()
      

fig,ax1 = plt.subplots()
plt.plot(X,f_seg,label='Seguros')
plt.plot(X,f_riesg,label='Riesgosos')
#plt.plot(X,cociente,label='cociente')
plt.legend(loc=0)
#ax2=ax1.twinx()
#plt.plot(X,maxim,'y',label='maxim')
#plt.legend(loc=1)

