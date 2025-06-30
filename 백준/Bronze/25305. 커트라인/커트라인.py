import sys

input = sys.stdin.readline
N, k = map(int, input().split())
xList = list(map(int, input().split()))

xList.sort(reverse = True)

print(xList[k - 1])