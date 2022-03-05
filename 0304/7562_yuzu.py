def bfs(a, b):
    q = [(a, b)]
    visited[a][b] == 1
    dx = [2, 2, -2, -2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, 2, 2, -2, -2]
    while q:
        x, y = q.pop(0)
        if x == ex and y == ey:
            return visited[x][y]
            break
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<l and 0<=ny<l and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

t = int(input())
for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[0] * l for i in range(l)]
    ans = bfs(sx, sy)
    print(ans)