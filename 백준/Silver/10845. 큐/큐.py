import sys


num = int(input())
stack = []
for i in range (num):
    command = sys.stdin.readline().split()

    if command[0] =='push':
        stack.append(command[1])

    elif command[0] =='front':
        if len(stack) <1 :
            print(-1)
        else : print(stack[0])

    elif command[0] =='back':
        if len(stack) <1 :
            print(-1)
        else : print(stack[-1])

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] =='pop':
        if len(stack) <1 :
            print(-1)
        else:
            print(stack.pop(0))

    elif command[0] == 'empty':
        if len(stack) < 1:
            print(1)
        else:
            print(0)