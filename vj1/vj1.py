import math
from tabulate import tabulate

def e1(x):
    e=0
    z=1
    k1=0
    epsilon=10**(-10)
    while abs(z) > epsilon:
        z=((-1)**k1)*(x**k1)/math.factorial(k1)      
        e+=z
        k1+=1
    return [e, k1]


def e2(x):
    k2=1
    e=0
    z=1
    sk=[1]
    epsilon=10**(-10)
    while abs(z) > epsilon:
        z=-sk[-1]*x/k2
        sk.append(z)
        k2+=1
    for i in range(len(sk)):
        e+=sk[i]
        
    NB=k2
    return [e, k2]

head=["x", "A", "B", "C", "D", "A članova", "B članova"]
mydata=[]

for i in range(11):
    y=10*i
    mydata.append([y, e1(y)[0], e2(y)[0], 1/e1(-y)[0], math.e**(-y), e1(y)[1], e2(y)[1]])

print(tabulate(mydata, headers=head, tablefmt="grid"))
