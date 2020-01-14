n = int(input())
s = input()

pre = s[:n//2]
post = s[n//2:]

if pre == post:
    print("Yes")
else:
    print("No")