import  sys

num = int(input())

list = list(map(int, sys.stdin.readline().split()))
stack = []
count = 0
for i in range(num):

    if not list[i] in stack:
        stack.append(list[i])
    else:
        count += 1

print(count)