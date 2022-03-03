def bfs(y, x):
    q = []
    q.append((y, x))
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    while q:
        y, x = q.pop(0)
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == 1:
                grid[ny][nx] = 0
                q.append((ny, nx))

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    grid = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        grid[b][a] = 1
    count = 0
    for x in range(m):
        for y in range(n):
            if grid[y][x] == 1:
                grid[y][x] = 0
                bfs(y, x)
                count += 1
    print(count)