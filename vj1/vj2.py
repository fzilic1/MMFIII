a1=[]
b1=[]
c1=[]
d1=[]

def solve(a, b, c, d, n):
    
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

    i=0
    while i <= n:
        x[i]=round(x[i]*94)
        i+=1

    return x

a=[0, 2, 2, 2]
b=[-4, -6, -6, -5]
c=[2 , 2, 2, 0]
d=[-5, 0, 0, 0]
 
print (solve(a, b, c, d, 4))

#-4I_1 + 2I_2               = -5
# 2I_1 - 6I_2 + 2I_3        = 0
#        2I_2 - 6I_3 + 2I_4 = 0
#               2I_3 - 5I_4 = 0
