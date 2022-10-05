import math

def e1(x):
    e=0
    z=1
    k=0
    epsilon=10**(-10)
    while abs(z) > epsilon:
        z=((-1)**k)*(x**k)/math.factorial(k)      
        e+=z
        k+=1
    return e

print (e1(4))

def e2(x):
    k=1
    e=0
    z=1
    sk=[1]
    epsilon=10**(-10)
    while abs(z) > epsilon:
        z=-sk[-1]*x/k
        sk.append(z)
        k+=1
    for i in range(len(sk)):
        e+=sk[i]
    return e

print (e2(4))

print (1/(math.e**4))