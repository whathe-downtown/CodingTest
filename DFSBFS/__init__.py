N,M,V = map(int,input().split()) # 4 5 1

matrix = [[0] * (N+1) for i in range(N+1)]

visited = [0] * (N+1)

for i in range(M):
    a,b= map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(V):
    # 방문한곳 1 넣기
    visited[V] = 1

    print(V, end=' ') # 한줄로 나열해서 출력할려고

    for i in range(1,N+1): #0 ~4
        if(visited[i] ==0 and matrix[V][i] ==1):
            dfs(i)

def bfs(V):
    queue = [V] # queue = [1]

    visited[V] = 0 # visited[1] = 0

    while queue:
        V = queue.pop(0)  # V = 1
        print(V,end=' ')
        for i in range(1,N+1):
            if(visited[i] == 1 and matrix[V][i] == 1):
                queue.append(i)
                visited[i] = 0
dfs(V)
print()
bfs(V)