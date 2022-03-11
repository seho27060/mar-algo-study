from collections import deque

n, k = map(int, input().split())

visited = [False] * (1000001)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 0
    while q:
        t = q.popleft()
        if t == k:
            return visited[t]
        for i in [t - 1, t + 1, t * 2]:
            if 0 <= i < 1000001 and not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1

cnt = bfs(n)
print(cnt)
