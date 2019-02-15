# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 23:44:48 2018

@author: MARIEM & CYRINE
"""

import numpy as np
import matplotlib.pyplot as plt      
import matplotlib.image as mpimg


from sklearn.metrics import mean_squared_error
from math import sqrt
import os

path="path to the test images fold"
allimages= os.listdir(path )[1:]

images=['vienna','tyrol-w','austin','chicago','kitsap']


errors=[]
for i in images:
    rms=0
    ct=0
    for j in range(37):
        if i+str(j)+'_real_B.png' in allimages:
            ct+=1
            a=mpimg.imread(path+"\\"+i+str(j)+'_real_B.png')
            b=mpimg.imread(path+"\\"+i+str(j)+'_fake_B.png')
            c=(a-b)**2
            rms+= np.sum(c)/(c.shape[0]*c.shape[1]*c.shape[2]) 
    errors.append(np.sqrt(rms/ct))
    
    
print("total error is", np.mean(errors))
     