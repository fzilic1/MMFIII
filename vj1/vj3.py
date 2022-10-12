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
