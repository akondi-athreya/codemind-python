def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n = list(map(int,input().split()))
num1 = n[0]
num2 = n[1]

result = lcm(num1, num2)
print(f"{result}")
