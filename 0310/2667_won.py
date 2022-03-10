import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt = 0

def bfs(i, j, cnt):
    q = []
    q.append([i, j])
    visited[i][j] = cnt
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 and visited[ni][nj] == False:
                q.append([ni, nj])
                visited[ni][nj] = cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            bfs(i, j, cnt)

print(cnt)
sol = [0] * (cnt + 1)
for c in range(1, cnt + 1):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == c:
                sol[c] += 1

sol.sort()
for i in range(1, cnt + 1):
    print(sol[i])
