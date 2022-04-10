a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum = 1

for i in a:
    sum *= i
for j in b:
    print(i-sum, end='')

