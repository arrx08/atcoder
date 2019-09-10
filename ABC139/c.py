# encoding: utf-8

N=int(input())
H=list(map(int, input().split()))

def get_distance(s,H):
    distance=0

    for i in range(s,len(H)-1):
        if H[i+1] <= H[i]:
            distance += 1
        else:
            break
    
    return distance

ans = 0
i=0

while i < N:
    t = get_distance(i,H)
    if ans < t:
        ans = t
    i += t + 1

print(ans)