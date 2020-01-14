n = int(input())

#(1,1)から一番長く移動しないといけないのは(1,n)の時
ans = n - 1

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        ans = min(ans, i + int(n/i) - 2)

print(ans)