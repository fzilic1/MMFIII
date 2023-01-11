import numpy as np
import matplotlib.pyplot as plt

g=9.81
l=0.2484902028828339
m=0.2
pi=3.141592653589793
T=2*np.pi/np.sqrt(g/l)

def thetaAn(t):
    theta=pi*np.cos(np.sqrt(g/l)*t)/45
    return theta

def dv(t, x, v):
    dv=-(g/l)*np.sin(x)
    return dv

def dx(t, x, v):
    dx=v
    return dx

def Euler(dx, dv, t0, y0, v0, tn, N):
    h=(tn-t0)/N
    y=y0
    t=t0
    v=v0
    Y=[y]
    T=[t]
    V=[v]
    i=1
    while i <= N:
        v+=dv(t, y, v)*h
        y+=dx(t, y, v)*h
        t=t0+i*h
        V.append(v)
        Y.append(y)
        T.append(t)
        i+=1
    return T, Y, V

def RK4(dx, dv, t0, y0, v0, tn, N):
    h=(tn-t0)/N
    t=t0
    y=y0
    v=v0
    T=[t0]
    Y=[y0]
    V=[v0]
    i=1
    while i <= N:
        k1v=dv(t, y, v)
        k1x=dx(t, y, v)
        k2v=dv(t0+(i-0.5)*h, y+k1x*h/2, v+k1v*h/2)
        k2x=dx(t0+(i-0.5)*h, y+k1x*h/2, v+k1v*h/2)
        k3v=dv(t0+(i-0.5)*h, y+k2x*h/2, v+k2v*h/2)
        k3x=dx(t0+(i-0.5)*h, y+k2x*h/2, v+k2v*h/2)
        k4v=dv(t0+i*h, y+k3x*h, v+k3v*h)
        k4x=dx(t0+i*h, y+k3x*h, v+k3v*h)
        v=v+(k1v+2*k2v+2*k3v+k4v)*h/6
        y=y+(k1x+2*k2x+2*k3x+k4x)*h/6
        t=t0+i*h
        V.append(v)
        Y.append(y)
        T.append(t)
        i+=1
    return T,Y,V

def an(t0, x0, tn, N):
    h=(tn-t0)/N
    t=t0
    T=[]
    X=[]
    A=x0
    while t <= tn:
        x=A*np.cos(np.sqrt(g/l)*t)
        T.append(t)
        X.append(x)
        t+=h

    return T, X


P=Euler(dx, dv, 19*T, 32*pi/180, 0, 20*T, 50)
Q=RK4(dx, dv, 19*T, 32*pi/180, 0, 20*T, 50)
a=an(19*T, 32*pi/180, 20*T, 5000)
plt.plot(P[0], P[1], color='green', label='Euler')
plt.plot(Q[0], Q[1], color='red', label='Runge-Kutta')
plt.plot(a[0], a[1], color='blue', label='analitički')
plt.legend()
plt.show()
