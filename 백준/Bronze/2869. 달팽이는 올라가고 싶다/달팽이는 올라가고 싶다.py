import math
import sys

A, B, V = map(int,sys.stdin.readline().split())

day = (V-B) / (A-B)
print(math.ceil(day))