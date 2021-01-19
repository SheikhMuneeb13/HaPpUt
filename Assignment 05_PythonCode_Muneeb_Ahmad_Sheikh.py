from numpy import *
import matplotlib.pyplot as plt
#get the radius of circle
#diameter  is given 6.1 units
d=6.1
r=d/2
t=linspace(0,2*pi)
plt.axis("equal")
x=r*cos(t);
y=r*sin(t);
plt.plot(x,y)
plt.show()

