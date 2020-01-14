n, k = map(int, input().split())
a = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]

a.sort()
f.sort(reverse=True)

ans = 0

for i in range(len(a)):
    if a[i] > k:
        a[i] -= k
        ans = a[i] * f[i] + 
        break
    else:
        k -= a[i]
        a[i] = 0