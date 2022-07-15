from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    
    # 중복 신고 제거 
    report = set(report)
    # 신고별 id 저장
    user = defaultdict(set) 
    
    # 신고당한 횟수 저장
    cnt = defaultdict(int)
    
    for r in report:
        a, b = r.split()
        user[a].add(b)
        
        cnt[b] += 1
        
    for i in id_list:
        result =0
        
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer