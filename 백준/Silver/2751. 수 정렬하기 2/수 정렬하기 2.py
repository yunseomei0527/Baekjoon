import sys

inputs = sys.stdin.readlines()
numList = []

for input in inputs[1:]:
    num = int(input)
    numList.append(num)
    
numList.sort()

for num in numList:
    print(num)