num = int(input())
count= []
for i in range(num):
    a,b,c = map(int,input().split())
    
    if a == b == c:
        count.append(10000+(a * 1000))
    elif a == b or a ==c:
        count.append(1000+ (a*100))
    elif b==c :
        count.append(1000+(b*100))
    else:
        count.append(100 * max(a,b,c))
print(max(count))