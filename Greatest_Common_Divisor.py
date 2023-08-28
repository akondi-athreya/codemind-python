n = list(map(int,input().split()))
gcd = 1
a = n[0]
b = n[1]
if a>b:
    z = a
else:
    z = b
for i in range(1,z+1):
    if(n[0]%i==0 and n[1]%i==0):
        gcd = i
print(gcd)