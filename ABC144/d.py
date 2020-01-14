import math

a,b,x = map(int, input().split())

capacity = a * b

if x / a > capacity * 0.5:
    tan = 2 * (b / a - x / pow(a, 3)) 
    print(math.degrees(math.atan(tan)))
else:
    tan = 2 * x / (a * pow(b, 2))
    print(90 - math.degrees(math.atan(tan)))