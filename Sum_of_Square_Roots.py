import math
a = list(map(int,input().split()))
sum1 = 0
for i in range(a[0],a[1]+1):
    sum1 += math.sqrt(i)
print("{:.2f}".format(sum1))