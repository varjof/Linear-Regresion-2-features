# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 21:52:36 2022

@author: johnf
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.close("all")
df=pd.read_excel("Datos 2 caracteristicas.xlsx")
df.info()

m=len(df) #Número de muestras

df["Area"]=df["Area"]/max(df["Area"])
df["Rooms"]=df["Rooms"]/max(df["Rooms"])


th0=26768
th1=123897
th2=47641

theta=np.array([th0,th1,th2])

alfa=0.01
for i in range(15000):
    theta=theta-np.array(
        [alfa*1/(m)*sum(((theta[0] + theta[1]*df["Area"]+theta[2]*df["Rooms"])-df["Price"])*1),
        alfa*1/(m)*sum(((theta[0] + theta[1]*df["Area"]+theta[2]*df["Rooms"])-df["Price"])*df["Area"]),
        alfa*1/(m)*sum(((theta[0] + theta[1]*df["Area"]+theta[2]*df["Rooms"])-df["Price"])*df["Rooms"])])
    J=1/(2*m)*sum(((theta[0] + theta[1]*df["Area"]+theta[2]*df["Rooms"])-df["Price"])**2)
    plt.plot(i,J,"ob")
print(theta)
plt.xlabel("Iteración")
plt.ylabel("J")




mallaA,mallaR=np.meshgrid(np.arange(0.2,1,0.01),np.arange(0.2,1,0.01))
h=theta[0] + theta[1]*mallaA+theta[2]*mallaR

ax = plt.figure(2).add_subplot(projection='3d')
ax.plot(df["Area"],df["Rooms"], df["Price"],"+")

plt.xlabel("Area")
plt.ylabel("Rooms")

ax.plot_surface(mallaA,mallaR,h,alpha=0.3)


