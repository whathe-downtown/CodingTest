from collections import deque
n = int(input())
num_list = deque([x for x in range(1,n+1)])


while len(num_list) >1:
    num_list.popleft()
    a = num_list.popleft()
    num_list.append(a)

print(num_list[0])

