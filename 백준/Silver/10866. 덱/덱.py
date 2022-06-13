from sys import stdin
from collections import deque

num = int(input())

deque = deque([])
for i in range(num):
    command = stdin.readline().split()

    if command[0] == "push_front":
        deque.appendleft(command[1])

    elif command[0] == "push_back":
        deque.append(command[1])

    elif command[0] == "pop_front":
        if len(deque) < 1:
            print(-1)
        else:
            a = deque.popleft()
            print(a)
    elif command[0] == "pop_back":
        if len(deque) < 1:
            print(-1)
        else:
            b = deque.pop()
            print(b)
    elif command[0] == "size":
        print(len(deque))

    elif command[0] == "empty":
        if len(deque) < 1:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(deque) < 1:
            print(-1)
        else:
            print(deque[0])
    elif command[0] == "back":
        if len(deque) < 1:
            print(-1)
        else:
            print(deque[-1])
