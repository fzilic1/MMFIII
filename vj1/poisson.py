import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

a=5.0
b=8.0
e0=8.854187817

def sigma(x, y):
    s=np.sin(x)*np.cos(y)/e0
    return s

def explicit(ut0, y0, Dy, M, x0, X, N):
    dx=(X-x0)/N
    dy=Dy
    alpha=dy**2/dx**2

    yspace=[]
    xspace=[]
    uxt=[[], []]


    i=0
    while i < N:
        uxt[0].append(ut0(x0+i*dx))
        xspace.append(x0+i*dx)
        i+=1

    i=1
    uxt[1].append(0)
    while i < N-1:
        uxt[1].append(-alpha/2*uxt[0][i+1] + (1+alpha)*uxt[0][i]-alpha/2*uxt[0][i-1] + dy**2*sigma(x0+i*dx, 0))
        i+=1
    uxt[1].append(0)
    
    j=0
    while j < M:
        yspace.append(y0+j*dy)
        j+=1

    i=1
    j=2
    while j < M:
        u=[0]
        i=1
        while i < N-1:
            u.append(-alpha*uxt[-1][i+1]+2*(1+alpha)*uxt[-1][i]-alpha*uxt[-1][i-1]-uxt[-2][i]-dy**2*sigma(x0+i*dx ,y0+j*dy))
            i+=1
        u.append(0)
        uxt.append(u)
        j+=1



    return yspace, xspace, uxt

def U0(x):
    rho=5
    return rho

E=explicit(U0, 0, 0.05, 160, 0, a, 50)
Y=E[0]
X=E[1]
U=E[2]

i=0
X, Y = np.meshgrid(X, Y)
U=np.array([np.array(Ui) for Ui in U], dtype=object)

fig = plt.figure()
ax=plt.axes(projection="3d", xlabel= 'x', ylabel='y', zlabel='U')
ax.plot_surface(X, Y, U)

plt.show()
