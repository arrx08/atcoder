import math

x, y = map(int, input().split())

if not (2*y - x) % 3 == 0:
    print(0)
else:
    b = (2*y - x) // 3 
    a = y - 2 * b
        
    for i in range(b):
        ans *= i