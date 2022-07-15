def solution(id_list, report, k):
    answer = [0] * len(id_list) # [0,0,0,0]
    reports = {x: 0 for x in id_list}
    #{'muxi: 0','frodo':0,'apeach':0,'neo': 0}
    
    for r in set(report):
        reports[r.split()[1]] += 1
    
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer