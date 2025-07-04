import sys

input = sys.stdin.readline
N = list(map(int, list(input().rstrip())))
N.sort(reverse = True)

for num in N:
    print(num, end = '')