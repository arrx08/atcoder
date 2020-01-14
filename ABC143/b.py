n = int(input())
d = list(map(int, input().split()))

d_sum = sum(d)

m = 0
for k in d:
    m += k **2
    
print((d_sum**2 - m)//2)
