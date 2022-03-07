n = int(input())
graph = [[] for _ in range(n+1)]
t, v = map(int, input().split())
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0]*(n+1)
q = [t]
visited[t] = 1
while q:
    x = q.pop(0)
    if x == v:
        break
    for y in graph[x]:
        if visited[y] == 0:
            visited[y] = visited[x]+1
            q.append(y)
if visited[v] == 0:
    print(-1)
else:
    print(visited[v]-1)