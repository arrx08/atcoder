n = int(input())
d = list(map(int, input().split()))

n = len(d)
ans = 0

for i in range(n):
    for  j in range(i+1,n):
        ans += d[i] * d[j]

print(ans)