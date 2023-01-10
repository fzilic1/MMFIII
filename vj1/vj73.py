import numpy as np
import matplotlib.pyplot as plt

g=9.81
l=0.2484902028828339
m=0.2
pi=3.141592653589793

def thetaAn(t):
    theta=pi*np.cos(np.sqrt(g/l)*t)/45
    return theta

def acc(t, theta):
    dx=-g*np.sin(theta)/l
    return dx

def vel(t, theta):
    dtheta=Euler(acc, 0, 4*pi/180, t, 100)[1][-1]
    return dtheta

def Euler(dy, t0, y0, tn, N):
    h=(tn-t0)/N
    y=y0
    t=t0
    Y=[y]
    T=[t]
    i=1
    while i <= N:
        y+=dy(t,y)*h
        t=t0+i*h
        Y.append(y)
        T.append(t)
        i+=1
    return T, Y

def RK4(dy, t0, y0, tn, N):
    h=(tn-t0)/N
    t=t0
    y=y0
    T=[t0]
    Y=[y0]
    i=1
    while i <= N:
        k1=dy(t, y)
        k2=dy(t0+(i-0.5)*h, y+k1*h/2)
        k3=dy(t0+(i-0.5)*h, y+k2*h/2)
        k4=dy(t0+i*h, y+k3*h)
        y=y+(k1+2*k2+2*k3+k4)*h/6
        t=t0+i*h
        Y.append(y)
        T.append(t)
        i+=1
    return T,Y

P=Euler(acc, 0, 4*pi/180, 10, 50)
plt.plot(P[0], P[1], color='green')
plt.show()
