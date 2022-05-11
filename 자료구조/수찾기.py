from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
M = map(int,stdin.readline().split())

for l in M:
    stdout.write("1\n") if l in N else stdout.write("0\n")