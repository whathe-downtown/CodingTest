from sys import stdin

input= stdin.readline
N,M = map(int,input().split())
num_list = list(map(int,input().split()))

step = M
window = sum(num_list[:step])
answer = window

for i in range(step, N):
    window += (num_list[i] - num_list[i - step])
    answer = max(answer, window)
print(answer)