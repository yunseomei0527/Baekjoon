import sys

input = sys.stdin.readline
N = int(input())

countSix = 0
count = 0
num = 666

while count < N:
    listN = list(str(num))
    countSix = 0
    for i in range(0, len(listN)):
        if listN[i] == '6':
            countSix += 1
        else:
            countSix = 0
            
        if countSix >= 3:
            count += 1
            break

            
    num += 1

print(num - 1)