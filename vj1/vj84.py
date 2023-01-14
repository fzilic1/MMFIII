import matplotlib.pyplot as plt

def solve(a, b, c, d, n):
    a1=[]
    b1=[]
    c1=[]
    d1=[]
    
    x=[]
    i=0
    while i < n:
        x.append(0)
        i+=1

    c1.append(c[0]/b[0])
    d1.append(d[0]/b[0])
    n=n-1
    i=1
    while i<n:
        c1.append(c[i]/(b[i]-a[i]*c1[i-1]))
        d1.append((d[i]-a[i]*d1[i-1])/(b[i]-a[i]*c1[i-1]))
        i+=1

    d1.append((d[n]-a[n]*d1[n-1])/(b[n]-a[n]*c1[n-1]))
    x[n]=d1[n]
    i=n-1
    
    while i >= 0:
        x[i]=d1[i]-c1[i]*x[i+1]
        i-=1

    return x

def CN(ut0, t0, Dt, M, x0, X, N, a):
    dx=(X-x0)/N
    dt=Dt
    alpha=a*dt/dx**2

    time=[t0]
    space=[]
    uxt=[[]]


    i=0
    while i < N:
        uxt[0].append(ut0(x0+i*dx))
        space.append(x0+i*dx)
        i+=1

    A=[0]
    b=[]
    c=[]
    i=1
    while i < N:
        b.append(2+2*alpha)
        A.append(-alpha)
        c.append(-alpha)
        i+=1
    
    b.append(1+2*alpha)
    c.append(0)

    j=1
    while j < M:
        d=[(2-2*alpha)*uxt[-1][0]+alpha*uxt[-1][1]]
        i=1
        while i < N-1:
            d.append(alpha*uxt[-1][i-1]+(2-2*alpha)*uxt[-1][i]+alpha*uxt[-1][i+1])
            i+=1

        d.append(alpha*uxt[-1][-2]+(2-2*alpha)*uxt[-1][-1])
        u=solve(A, b, c, d, N)
        uxt.append(u)
        j+=1


    return time, space, uxt

def rhox0(x):
    if x>=2 and x<=5:
        rho=5.5
    else:
        rho=0
    return rho

E=CN(rhox0, 0, 0.5, 450, 0, 20, 200, 0.01)
T=E[0]
X=E[1]
U=E[2]

plt.plot(X, U[0], label='t=0')
plt.plot(X, U[100], label='t=100dt')
plt.plot(X, U[200], label='t=200dt')
plt.plot(X, U[300], label='t=300dt')
plt.plot(X, U[400], label='t=400dt')

plt.xlabel('x (m)')
plt.ylabel('rho(x, t) (kg/m)')
plt.title('Crank-Nicolsonova metoda')
plt.legend()
plt.show()
