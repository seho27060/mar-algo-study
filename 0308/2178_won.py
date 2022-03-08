n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(i, j):
    q = []
    visited[i][j] = 1
    q.append([i, j])
    while q:
        i, j = q.pop(0)
        if i == n - 1 and j == m - 1:
            return visited[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == False:
                visited[ni][nj] = visited[i][j] + 1
                q.append([ni, nj])
cnt = bfs(0, 0)
print(cnt)