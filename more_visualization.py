import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# using pyplot API for visualization
#1. Global API
x = np.arange(-10,11)
plt.figure(figsize=[12, 6])

plt.title("My nice Plot")
plt.subplot(1,2,1)
plt.plot(x, x ** 2)
plt.plot([0,0,0],[-10,0,10])# drawing a straight line
plt.legend(['x^2','Vertical line'])
plt.subplot(1,2,2)
plt.plot(x, -1*(x ** 2))
plt.plot([0,0,0],[-10,0,10])# drawing a straight line
plt.legend(['-x^2','Vertical line'])
plt.show()



#2. OOP API
fig,axes = plt.subplots(figsize=[12,6])
axes.plot(x, (x ** 2), color='red', marker='o', markersize='8', linewidth= 3, label='X^2')
axes.plot(x, -1 * (x ** 2),label = '-X^2',linestyle ='--', color='blue')
axes.set_title("My nice plot")
axes.legend()
plt.show()


#CREATING A SCATTER PLOT USING OOP API
N = 50
x=np.random.rand(N)
y=np.random.rand(N)

color = np.random.rand(N)
area = np.pi * (20*np.random.rand(N)) **2 #0 to 15 radii
#plt.figure(figsize=[14,6])
plt.scatter(x, y, c=color, alpha=0.5, s=area,cmap='Spectral')
plt.colorbar()
plt.show()


#CREATING AN HISTOGRAM

values = np.random.randn(1000)
plt.figure(figsize = [12,6])
plt.hist(values, histtype='bar',edgecolor = 'blue', bins=100,alpha = 0.8, color='steelblue')
plt.xlim(xmin=-7, xmax=5)
plt.show()


#CREATING BAR PLOT
Y= np.random.rand(1,5)[0]
Y2= np.random.rand(1,5)[0]
plt.figure(figsize =[12,6])
plt.bar(np.arange(len(Y)),Y,width=0.5, color = 'lightgreen')
plt.show()