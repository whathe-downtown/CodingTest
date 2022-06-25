from sys import stdin
a, b= map(int,input().split())
arr = []
for i in range(a):
    coin = int(stdin.readline())
    arr.append(coin)

_arr = arr[::-1]
count = 0
for i in _arr:
    count += b // i
    b %= i
print(count)