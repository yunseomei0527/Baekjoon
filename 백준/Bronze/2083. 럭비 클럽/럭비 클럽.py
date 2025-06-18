import sys
inputs = sys.stdin.readlines()

for input in inputs[:-1]:
    name, age, weight = input.split()
    age = int(age)
    weight = int(weight)
    
    if age <= 17 and weight < 80:
        print(name + " Junior")
        
    else:
        print(name + " Senior")