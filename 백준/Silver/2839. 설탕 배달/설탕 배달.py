import sys

input = sys.stdin.readline
N = int(input())
i = 0
j = 0
numList = []

while 5 * i <= N:
    j = 0
    while 3 * j <= N:
        if (5 * i) + (3 * j) == N:
            numList.append(i + j)
        j += 1
    i += 1
    
numList.sort()
if len(numList) == 0:
    print(-1)
else:
    print(numList[0])