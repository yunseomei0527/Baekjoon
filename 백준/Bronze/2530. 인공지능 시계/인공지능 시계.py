import sys

input = sys.stdin.readline
H, M, S = map(int, input().split())
cook_S = int(input())

time_S = ((H * 3600) + (M * 60) + S) + cook_S

while True:
    if time_S >= (24 * 3600):
        time_S -= (24 * 3600) 
        
    else:
        h = time_S // 3600
        m = ((time_S) % 3600) // 60
        s = ((time_S) % 3600) % 60
        break
    
print(h, end = ' ')
print(m, end = ' ')
print(s)