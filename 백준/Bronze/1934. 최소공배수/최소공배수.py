import math
from sys import stdin

input= stdin.readline
num = int(input())

for i in range(num):
    a ,b = map(int,input().split())
    print(math.lcm(a,b))