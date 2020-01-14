n,k,m = map(int,input().split())

a = list(map(int, input().split()))

ans = n * m - sum(a)

if ans > k:
    print(-1)
elif ans < 0:
    print(0)
else:
    print(ans)
