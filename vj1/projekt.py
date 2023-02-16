import numpy as np
import matplotlib.pyplot as plt

e0=8.854187817

#raspodjela naboja
def sigma(x, y):
    s=(10**4)*np.sin(x)*np.cos(y)/e0
    #s=x**2-y**2
    #s=y**2*np.sqrt(np.sin(x)**2)
    return s

#jacobijeva metoda
def jacobi(ut0, y0, Dy, M, x0, Dx, N):
    maxI=100000
    dx=Dx
    dy=Dy

    yspace=[]
    xspace=[]
    uxt=[[]]

    #rubni uvjeti i aproksimacija
    i=0
    while i < N:
        uxt[0].append(ut0(x0+i*dx))
        xspace.append(x0+i*dx)
        i+=1
    
    j=0
    while j < M:
        yspace.append(y0+j*dy)
        j+=1

    j=1
    while j < M:
        u=[0]
        i=1
        while i < N-1:
            u.append(0)
            i+=1
        u.append(0)
        uxt.append(u)
        j+=1
    
    #iteracija
    Iter=0
    diff=1.0
    while Iter <= maxI and diff > 0.000001:
        Utemp=uxt
        diff=0.
        j=1
        while j < M-1:
            i=1
            while i < N-1:
                uxt[j][i]=0.25*(Utemp[j+1][i]+Utemp[j-1][i]+Utemp[j][i+1]+Utemp[j][i-1])+(dx**2/4)*sigma(x0+i*dx, y0+j*dy)
                diff+= np.abs(Utemp[j][i]-uxt[j][i])
                i+=1
            j+=1

        Iter+=1
        diff=diff/(N*M)



    return yspace, xspace, uxt


def U0(x):
    rho=0
    return rho

E=jacobi(U0, 0, 0.1, 100, 0, 0.1, 100)
Y=E[0]
X=E[1]
U=E[2]

i=0
X, Y = np.meshgrid(X, Y)
U=np.array([np.array(Ui) for Ui in U], dtype=object)

fig = plt.figure()
ax=plt.axes(projection="3d", xlabel= 'x [m]', ylabel='y [m]', zlabel='U [V]')
ax.plot_surface(X, Y, U, cmap='autumn')

plt.show()
