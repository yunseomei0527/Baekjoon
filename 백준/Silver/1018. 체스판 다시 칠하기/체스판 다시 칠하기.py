import sys

inputs = sys.stdin.readlines()
bord = []
N, M = map(int, inputs[0].split())
mini = float("inf")

for input in inputs[1 :]:
    bord.append(list(input.rstrip()))
    
for i in range(0, N - 7): 
    for j in range(0, M - 7):
        flagW = 'B'
        flagB = 'W'
        countW = 0
        countB = 0
        
        # 한 체스판에서의 각각의 정사각형
        for y in range(i, i + 8):
            for x in range(j, j + 8):
                flag = (x + y) % 2
                # 완성된 체스판의 첫 번째 칸이 하얀색인 경우
                if flag:
                    if bord[y][x] == 'W':
                        countW += 1
                    
                else:
                    if bord[y][x] == 'B':
                        countW += 1
                        
                # 완성된 체스판의 첫 번째 칸이 검은색인 경우    
                if flag:
                    if bord[y][x] == 'B':
                        countB += 1
                    
                else:
                    if bord[y][x] == 'W':
                        countB += 1
        tempMin = min([mini, countW, countB])
        if  tempMin!= mini:
            mini = tempMin
            
print(mini)