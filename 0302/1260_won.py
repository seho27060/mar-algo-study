n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
# print(graph)
def dfs(v):
    visited[v] = True
    stack.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
stack = []
visited = [False] * (n + 1)
dfs(v)
print(*stack)


visited = [0] * (n + 1)
arr = []
def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        arr.append(t)
        for i in graph[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1
bfs(v)
print(*arr)