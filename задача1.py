import numpy as np
import matplotlib.pyplot as plt
n,r,x0=map(float,input().split())
y=[x0]
a=[1]
def f(x):
    y=4*r*x*(1-x)
    return y
for i in range (int(n)-1):
    a.append(i+1)
    y.append(f(y[-1]))
plt.plot(a,y)
plt.show()
