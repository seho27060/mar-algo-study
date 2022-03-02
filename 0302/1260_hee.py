N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
# 양방향 그래프
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
# dfs
def dfs(V):
    s = V
    ST = [s]
    result = []
    visited = [False] * (N+1)
    while ST:
        s = ST.pop()
        visited[s] = True
        result.append(s)
        for i in G[s]:
            if not visited[i]:
                ST.append(i)
        while ST and visited[ST[-1]]:
            ST.pop()
    return result
# bfs
def bfs(V):
    s = V
    ST = [s]
    result = []
    visited = [False] * (N+1)
    while ST:
        s = ST.pop(0)
        visited[s] = True
        result.append(s)
        for i in G[s]:
            if not visited[i]:
                ST.append(i)
        while ST and visited[ST[0]]:
            ST.pop(0)
    return result

# 정점 번호가 작은 것부터 방문하도록 sort 처리
for i in G:
    i.sort(reverse=True)
print(*dfs(V))
for i in G:
    i.sort()
print(*bfs(V))