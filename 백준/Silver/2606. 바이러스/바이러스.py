#DFS
from sys import stdin

input= stdin.readline
n= int(input()) #정점Vertax
m= int(input()) #간선 
graph =[ [] for _ in range(n+1)] 
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited =[0] * (n+1)
                    
def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph,i,visited)
    return True

dfs (graph,1,visited)
print(sum(visited)- 1)