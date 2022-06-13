from collections import deque
n = int(input())
num_list = deque([x for x in range(1,n+1)])
num_list.reverse()

while len(num_list) >1:
    num_list.pop()
    a = num_list.pop()
    num_list.insert(0,a)

print(num_list[0])

