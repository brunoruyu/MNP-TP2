# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 12:47:42 2017

@author: bruno
"""
import numpy as np
import pandas as pd
    

def ReadCsv(archivo):
    cols=['Indice','Z','Riesgo']
    df=pd.read_csv(archivo,header=None,sep="\t",decimal=".")
    df.columns=cols
    #ret=ajustadf(df)
    buenos=df[df['Riesgo']==0]
    malos=df[df['Riesgo']==1]
    return df,buenos,malos
    
