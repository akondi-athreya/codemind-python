n = int(input())
c = 0
for i in range(2,(n//2)+1):
    if n%i==0:
        print("Not Prime")
        break
    else:
        c+=1
if c>0:
    print("Prime")