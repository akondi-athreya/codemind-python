a = list(map(int,input().split()))
c = 0
for i in range(a[0],a[1]+1):
    if i%3==0:
        c+=1
print(c)