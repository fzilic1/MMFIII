import matplotlib.pyplot as plt

a=[]
b=[]

file=open("V(H-H).txt", "r")
l=1
for line in file:
    if l > 2:
        podaci=[float(x) for x in line.split()]
        a.append(podaci[0])
        b.append(podaci[1])
    l+=1
file.close

file = open("V(H-H)_AK.txt", "w")

for i in range(len(a)):
    a[i]=a[i]*0.52917721092
    b[i]=b[i]*315775.04
    file.write("%8.11f\t%8.11f\n" %(a[i], b[i]))

file.close()

def lagrange(ax, by, N, x, y):
    for i in range(N):
        L=1
        for j in range(N):
            if j != i:
                L=L*(x-ax[j])/(ax[i]-ax[j])

        y+=by[i]*L
    return y


k=7/71
z=2.81
file = open("V(H-H)_inter.txt", "w")
while z <= 9.81:
    Y=0
    Y=lagrange(a, b, len(a), z, Y)
    
    file.write("%8.11f\t%8.11f\n" %(z, Y))
    
    
    z+=k

file.close()

x_data=[]
y_data=[]
x_inter=[]
y_inter=[]

file=open("V(H-H)_AK.txt", "r")
l=1
for line in file:
    if l>9:
        podaci=[float(x) for x in line.split()]
        x_data.append(podaci[0])
        y_data.append(podaci[1])
    l+=1
file.close()

file=open("V(H-H)_inter.txt", "r")
for line in file:
    podaci=[float(x) for x in line.split()]
    x_inter.append(podaci[0])
    y_inter.append(podaci[1])
file.close()

plt.plot(x_data, y_data, 'o', label='Zadani podatci')
plt.plot(x_inter, y_inter, 'x', ms=5, label='Interpolacija')
plt.xlabel("r / A")
plt.ylabel("V / K")
plt.legend()
plt.show()
