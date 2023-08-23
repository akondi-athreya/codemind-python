import math
z = list(map(int,input().split()))
a = z[0]
b = z[1]

x = pow(10,b)
q = a % x
e = str(a)[::-1]
r = int(e)
t = b
rem = 0
k=[]
while(t!=0):
    rem = r % 10
    x //= 10
    k.append(rem*x)
    
    r //= 10
    t-=1

u = sum(k)
print(abs(u-q))
