from sys import stdin

num = int(input())
first = list(map(int, stdin.readline().split()))
second = list(map(int, stdin.readline().split()))

count = 0


first.sort()
second.sort(reverse=True)

for i in range(num):
    count += (first[i] * second[i])

print(count)