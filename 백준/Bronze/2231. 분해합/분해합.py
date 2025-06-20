import sys

input = sys.stdin.readline
N = int(input())
x = len(str(N))
start = max(0, N - x * 9)
answer = 0

for i in range(start, N + 1):
    iList = list(map(int, list(str(i))))
    sumList = i + sum(iList)
    
    if sumList == N:
        answer = i
        break

print(answer)