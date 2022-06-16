num = int(input())
_list = list(map(int, input().split()))
_list.sort()
sum = 0 

for i in range(num):
    for j in range(i+1):
        sum += _list[j]

print(sum)       