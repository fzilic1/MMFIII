import matplotlib.pyplot as plt

#difuzijska jednadžba
def explicit(ut0, t0, Dt, M, x0, X, N, a):
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

    i=1
    j=1
    while j < M:
        u=[0]
        i=1
        while i < N-1:
            u.append(alpha*uxt[-1][i+1] + (1-2*alpha)*uxt[-1][i] + alpha*uxt[-1][i-1])
            i+=1
        u.append(0)
        uxt.append(u)
        time.append(t0+j*dt)
        j+=1



    return time, space, uxt

def rhox0(x):
    if x>=2 and x<=5:
        rho=5.5
    else:
        rho=0
    return rho

E=explicit(rhox0, 0, 0.5, 450, 0, 20, 150, 0.01)
T=E[0]
X=E[1]
U=E[2]
i=0

plt.plot(X, U[0], label='t=0')
plt.plot(X, U[100], label='t=100dt')
plt.plot(X, U[200], label='t=200dt')
plt.plot(X, U[300], label='t=300dt')
plt.plot(X, U[400], label='t=400dt')

plt.xlabel('x (m)')
plt.ylabel('rho(x, t) (kg/m)')
plt.title('Eksplicitna metoda')
plt.legend()
plt.show()
