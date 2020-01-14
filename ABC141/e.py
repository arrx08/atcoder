n=int(input())
s=input()


z = [0] * n

L,R= 0,0
z[0] = n

for i in range(1,n):
    if i > R:
        L=i; R=i
        while R < n and s[R] == s[R-L]:
            R += 1
        z[i] = R - L
        R -= 1
    else:
        k = i - L
        if z[k] < R-i+1:
            z[i] = z[k]
        else:
            L = i
            while R < n and s[R] == s[R-L]:
                z[i] = R - L
                R -= 1

print(z)
