n = int(input())
a= list(map(int, input().split()))

c = 0
r = []
num = 1

for i in range(n):
    if a[i] == num:
        r.append(a[i])
        num += 1
    else:
        c +=1

if r == []:
    print(-1)
else:
    print(c)


