from sys import stdin

num = int(input())
dic = {}

for i in range(num):
    a = stdin.readline()
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] +=1
list = []
num = max(dic.values())

for i in dic:
    if num == dic[i]:
        list.append(i)

list.sort()
print(list[0])