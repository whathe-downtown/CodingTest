num , limit_age = map(int,input().split())
arr= list(map(int,input().split()))
result= 0
for i in range(num):
    for j in range(i+1,num):
        for k in range(j+1, num):
            if arr[i] + arr[j] + arr[k] > limit_age:
                continue
            else:
                result = max(result,arr[i]+arr[j]+arr[k])
print(result)