num = int(input())

weight_list = []
for i in range(num):
    player = list(map(int,input().split()))
    weight_list.append(player)

for i in weight_list:
    rank = 1
    for j in weight_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")