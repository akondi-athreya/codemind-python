import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
a = (x2-x1)*(x2-x1)
b = (y2-y1)*(y2-y1)
c = math.sqrt(a+b)
print(format(c,".4f"))