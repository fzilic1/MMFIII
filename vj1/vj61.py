import numpy as np

def func(x):
    y=x**3
    return y

def trapez(f, a, b, m):
    h=(b-a)/m
    k=1
    y=0.5*f(a)+0.5*f(b)
    while k < (m-2):
        y+=f(a+k*h)
        k+=1

    y=h*y
    return y

print (trapez(func, 0, 2, 4))

def simpson(f, a, b, m):
    h=(b-a)/m
    k=1
    y=f(a)+f(b)
    while k < (m-2):
        if (k%2)==0:
            y+=2*f(a+k*h)
        else:
            y+=4*f(a+k*h)

        k+=1
    
    y=(h/3)*y
    return y

print (simpson(func, 0, 2, 4))
