from sys import stdin

input = stdin.readline
low = int(input())
high = int(input())
sosu_list = []

for i in range(low,high+1):
    error = 0
    if i > 1 :
        for j in range(2,i):
            if  i % j == 0 :
                error += 1
                break
        if error == 0:
            sosu_list.append(i)

if len(sosu_list) > 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)

