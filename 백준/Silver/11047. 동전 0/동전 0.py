from sys import stdin

a, b = map(int,input().split())
array = []
count = 0
for i in range(a):
    put = int(stdin.readline().rstrip())
    array.append(put)

array.sort(reverse= True)
for i in array:
    if b >= i:
        count += b // i
        b %= i
        if i <= 0:
            break

print(count)