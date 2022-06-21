from sys import stdin

arr = [int(stdin.readline().rstrip()) for i in range(9)]
arr.sort()

for i in range(9):
    for j in range(i+1 , 9):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            for k in range(9):
                if i ==k or j == k:
                    continue
                print(arr[k])
            exit()