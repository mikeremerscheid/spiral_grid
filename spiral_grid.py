# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 18:06:30 2022

@author: miker
"""

# Define the starting centerpoint as x and y
# Set destination for how many loops

from matplotlib import pyplot as plt


plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["figure.autolayout"] = True
x = 0
y = 0
lon = []
lat = []
lon.append(x)
lat.append(y)   
destination = 1
radius = 10
for count, (cycle) in enumerate(range(0, radius), start=1):
    print('\nNew cycle.')
  
    x += destination
    print('Going right.')
    for step in range(x, x+destination, 1):
      print(f'{count}: lat: {y}, lon: {step-destination+1}')
      lon.append(x)
      lat.append(y)    

    y -= destination
    print('Going down.')
    for step in range(y, y-destination, -1):  
      print(f'{count}: lat: {step+destination-1}, lon: {x}')
      lon.append(x)
      lat.append(y)   

    destination += 1

    x -= destination
    print('Going left.')
    for step in range(x, x-destination, -1):
      print(f'{count}: lat: {y}, lon: {step+destination-1}')
      lon.append(x)
      lat.append(y)   

    y += destination
    print('Going up.')
    for step in range(y, y+destination, 1):
      print(f'{count}: lat: {step-destination+1}, lon: {x}')
      lon.append(x)
      lat.append(y)   

    destination+=1 

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid()
plt.plot(lon, lat, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
plt.show()
  
