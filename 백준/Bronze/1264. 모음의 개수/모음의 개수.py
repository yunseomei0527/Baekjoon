import sys

inputs = sys.stdin.readlines()

for input in inputs[:-1]:
    count = 0
    input = input.replace(" ", "").rstrip().lower()
    for i in input:
        if i in ['a','i','u','e','o']:
            count += 1
    print(count)