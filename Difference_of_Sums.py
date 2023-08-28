n = int(input())
sum1 = 0
sum2 = 0
for i in range(1,n+1):
    sum1 += i*i
    sum2 += i
print((sum2*sum2)-sum1)