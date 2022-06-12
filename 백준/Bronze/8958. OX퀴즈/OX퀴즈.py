from sys import stdin

num = int(input())

for i in range(num):
    case= str(stdin.readline())
    count = 0
    sum = 0
    for j in list(case):
        if j== "O":
            count += 1
            sum += count
        else:
            count= 0
        
    print(sum)
    

    