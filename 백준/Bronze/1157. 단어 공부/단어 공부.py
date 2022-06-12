case = input().upper()
case_set = list(set(case))
cnt= []

for i in case_set:
    cnt.append(case.count(i))
    
if cnt.count(max(cnt)) > 1:
    print("?")
    
else:
    print(case_set[cnt.index(max(cnt))])