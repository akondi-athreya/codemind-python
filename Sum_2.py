n = list(map(int,input().split()))
a = n[0]
b = n[1]
x = n[2]
y = n[3]
sum1=0
for i in range(a,b+1):
    if(i%x==0 and i%y!=0):
        sum1 += i
print(sum1)