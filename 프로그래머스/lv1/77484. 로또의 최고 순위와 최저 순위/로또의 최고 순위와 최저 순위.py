def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    cnt_0 = lottos.count(0)
    overlap = 0
    for i in lottos:
        if i in win_nums:
            overlap += 1
    return rank[overlap+cnt_0],rank[overlap]

