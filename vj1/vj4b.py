import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

def der2(f, x, h):
    df=(f(x+h)-2*f(x)+f(x-h))/(h**2)
    return df

def func(x):
    return np.exp(x)

x=[]
h=[]
for i in range(11):
    x.append(i)   
for i in range(6):
    h.append(1.0/np.power(10, i+1))

xtemp=[]
errtemp=[]
err=[]
X=[]
z=-1
for i in h:
    z+=1
    xtemp.append(h[z])
    for j in x:
        xtemp.append(der2(func, j, i))
        errtemp.append(np.absolute(xtemp[-1]-np.exp(j)))
    X.append(xtemp)
    err.append(errtemp)
    errtemp=[]
    xtemp=[]

ex=["e^x"]
for i in x:
    ex.append(np.exp(i))

X.append(ex)

head=["h"]
for i in x:
    head.append(i)

#print(tabulate(X, headers=head, tablefmt="grid"))

print(err[5][5])
