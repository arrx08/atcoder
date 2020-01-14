n = int(input())

if n % 2 > 0:
    print(0)
    exit()

ans = 0

for i in range(n//2):
    if (i+1) % 5 == 0:
        ans += 1

print(ans)