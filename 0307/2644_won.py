n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(v):
    q = []
    visited[v] = 0
    q.append(v)
    while q:
        t = q.pop(0)
        if t == b:
            return visited[t]
        for i in arr[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1
    return -1

visited = [False] * (n + 1)
cnt = bfs(a)

print(cnt)