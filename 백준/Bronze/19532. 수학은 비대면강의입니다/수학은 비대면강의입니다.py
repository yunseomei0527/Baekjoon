import sys

input = sys.stdin.readline
a, b, c, d, e, f = map(int, input().split())

for _x in range(-999, 1000):
    for _y in range(-999, 1000):
        if a * _x + b * _y == c and d * _x + e * _y == f:
            x = _x
            y = _y
            break
        
        else:
            continue
    
print(int(x), int(y), sep = ' ')