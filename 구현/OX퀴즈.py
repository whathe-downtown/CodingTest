a = int(input())

for i in range(a):
    b= list(input())
    cnt = 0
    sum_cnt = 0
    for j in b:
        if j == "O":
            cnt += 1
            sum_cnt += cnt
        else:
            cnt = 0
    print(sum_cnt)