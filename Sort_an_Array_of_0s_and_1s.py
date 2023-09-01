n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
for i in range(0,len(b)):
    print(b[i],end=" ")
    