n = int(input())
s = input()

pre = s[0]
ans = []
ans.append(pre)

for i in range(1,n):
    if not s[i] == pre:
        ans.append(s[i])
    pre = s[i]

print(len(ans))
