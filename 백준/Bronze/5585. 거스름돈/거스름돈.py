arr = [500,100,50,10,5,1]
num = 1000 - int(input())
count = 0
for i in arr:
    count += num // i
    num %= i
print(count)