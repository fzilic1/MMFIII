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

def gauleg(f, a, b, n):
    x, w =np.polynomial.legendre.leggauss(n)
    i=0
    
    t = 0.5*(x + 1)*(b - a) + a

    y=sum(w*f(t))*0.5*(b - a)

    return y

def Maxwell(v):
    T=300
    k=1.38064e-23
    m=3.37e-26
    M=1.8518304e-8*v**2*np.exp((-m*v**2)/(2*k*T))

    return M

print (trapez(Maxwell, 509.4, 609.4, 2000))
print (simpson(Maxwell, 509.4, 609.4, 2000))
print (gauleg(Maxwell, 509.4, 609.4, 200))
