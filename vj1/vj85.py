import matplotlib.pyplot as plt
import numpy as np

def explicit(ut0, t0, Dt, M, x0, X, N, a):
    dx=(X-x0)/N
    dt=Dt
    alpha=a*dt**2/dx**2

    time=[t0, t0+dt]
    space=[]
    uxt=[[], []]


    i=0
    while i < N:
        uxt[0].append(ut0(x0+i*dx))
        uxt[1].append(ut0(x0+i*dx))
        space.append(x0+i*dx)
        i+=1

    i=1
    j=2
    while j < M:
        u=[0]
        i=1
        while i < N-1:
            u.append(alpha*uxt[-1][i+1] + (2-2*alpha)*uxt[-1][i] + alpha*uxt[-1][i-1] - uxt[-2][i])
            i+=1
        u.append(0)
        uxt.append(u)
        time.append(t0+j*dt)
        j+=1



    return time, space, uxt

def rhox0(x):
    rho=np.exp(-400*(x-0.3)**2)
    return rho

E=explicit(rhox0, 0, 0.01, 100, 0, 1.0, 100, 1)
T=E[0]
X=E[1]
U=E[2]
i=0

plt.plot(X, U[0], label='t=0')
plt.plot(X, U[5], label='t=0.05')
plt.plot(X, U[10], label='t=0.1')
plt.plot(X, U[20], label='t=0.2')

plt.xlabel('x')
plt.ylabel('u(x, t)')
plt.title('Valna jednadžba')
plt.legend()
plt.show()
