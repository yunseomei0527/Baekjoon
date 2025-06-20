import sys

input = sys.stdin.readline
N = int(input())
answer = 0

for i in range(0, N):
    box = list(str(i))
    box = list(map(int, box))
    boxSum = i + sum(box)
    
    if boxSum == N:
        answer = i
        break
    

print(answer)