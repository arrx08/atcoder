a,b = list(map(int,input().split()))

# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

def factorize(n):
    b = 2
    factor=[]
    while b * b <= n:
        while n % b == 0:
            n //= b
            factor.append(b)
        b += 1
    if n > 1:
        factor.append(n)
    return factor

while b:
    a, b = b, a % b

print(len(set(factorize(a)))+1)
