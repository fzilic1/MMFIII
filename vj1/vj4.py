import numpy as np
from tabulate import tabulate

def der1(f, x, h, method):
    if method=='nap' or '2':
        df=(f(x+h)-f(x))/h
    if method=='naz':
        df=(f(x)-f(x-h))/h
    if method=='c' or '3':
        df=(f(x+h)-f(x-h))/(2*h)
    if method=='5':
        df=(-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
    
    return df

def func(x):
    return np.exp(x)

x=[0.5, 1.5, 2.5]
h=[0.1, 0.001, 0.00001]

head=["h"]
for i in x:
    head.append(i)

xtemp=[]
X=[]
z=-1
for i in h:
    z+=1
    xtemp.append(h[z])
    for j in x:
        xtemp.append(der1(func, j, i,'5'))
    X.append(xtemp)
    xtemp=[]

print(tabulate(X, headers=head, tablefmt="grid"))
