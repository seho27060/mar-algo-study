from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b, h):
    q = deque()
    q.append([a, b])
    visited[a][b] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] > h and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append([nx, ny])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max = 0
for ar in arr:
    for r in ar:
        if r > max:
            max = r

ans = 0
for h in range(max):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for a in range(n):
        for b in range(n):
            if arr[a][b] > h and visited[a][b] == 0:
                bfs(a, b, h)
                cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)