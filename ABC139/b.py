# encoding: utf-8

A, B = map(int, input().split())

ans=0
socket=1

while True: 
    if socket >= B:
        break
    else:
        socket += A - 1
        ans += 1

print(ans)

   

