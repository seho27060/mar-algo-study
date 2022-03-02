graph = {}
n, m, v = map(int, input().split())
for i in range(1, n+1):
    graph[i] = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for key in graph:
    graph[key].sort()

def dfs(v):
    visit = []
    stack = [v]
    while stack:
        x = stack.pop()
        if x not in visit:
            visit.append(x)
            stack.extend(reversed(graph[x]))
    return visit

def bfs(v):
    visit = [v]
    q = [v]
    while q:
        x = q.pop(0)
        for y in graph[x]:
            if y not in visit:
                visit.append(y)
                q.append(y)
    return visit

print(*dfs(v))
print(*bfs(v))