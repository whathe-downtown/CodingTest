a = int(input())
number = list(map(int,input().split()))
b = int(input())
compare_number = list(map(int,input().split()))

for i in compare_number:
    if i in number:
        print(1)
    else:
        print(0)
