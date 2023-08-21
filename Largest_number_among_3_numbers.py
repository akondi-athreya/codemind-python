a = list(map(int,input().split()))
if(a[0]>a[1]>a[2] or a[0]>a[2]>a[1]):
    print(a[0])
elif(a[1]>a[0]>a[2] or a[1]>a[2]>a[0]):
    print(a[1])
else:
    print(a[2])