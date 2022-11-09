import numpy as np

def y1(t):
    y=5.0+np.cos(3.0*t)-0.325-2.0*np.exp(0.5*t)
    return y

def dy1(t):
    y=-3.0*np.sin(3.0*t)-np.exp(0.5*t)
    return y

def bisekcija(func, epsilon, a, b):
    a=a
    b=b
    c=(a+b)/2
    n=0
    while abs(func(c)) >= epsilon:
        if func(a)*func(c) < 0:
            b=c
        else:
            a=c
        c=(a+b)/2
        n+=1

    return [c, n]

print (bisekcija(y1, 0.0001, 0, 1000))

def Newton(func, der, epsilon, x0):
    x=x0
    n=0
    while abs(func(x)/der(x)) >= epsilon:
        x=x-(func(x)/der(x))
        n+=1

    return [x, n]

print (Newton(y1, dy1, 0.0001, 8))   
