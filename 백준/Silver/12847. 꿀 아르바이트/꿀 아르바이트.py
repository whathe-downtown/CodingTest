from sys import stdin
input= stdin.readline
N, M = map(int,input().split()) # N =5, M= 3
number_list = list(map(int,input().split()))

step = M
window = sum(number_list[:step])
answer= window
for i in range(step, N):
    window += (number_list[i] - number_list[i-step])
    answer = max(answer, window) # 둘 중 max 값을 비교 

print(answer)
    
    
