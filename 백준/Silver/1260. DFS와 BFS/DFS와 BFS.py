from sys import stdin
from collections import deque

# Settings
input = stdin.readline
N, M, V = map(int, input().split())  # 4 , 5, 1
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)


# DF

def dfs(n):
    visited[n] = True
    print(n, end=' ')
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

# BFS
def bfs(n):
    queue = deque([n])
    visited[n] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(V)
# 한칸 뛰기
print()
# visited 초기화
visited = [False] * (N+1)

bfs(V)
