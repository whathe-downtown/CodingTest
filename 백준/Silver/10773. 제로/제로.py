from sys import  stdin
num = int(input())
stack = []

for i in range(num):
    says = int(stdin.readline().rstrip())

    if says == 0:
        stack.pop()
    else:
        stack.append(says)

print(sum(stack))
