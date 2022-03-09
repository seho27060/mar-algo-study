n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
road = [[0, 0]]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited[0][0] = 1
while road:
    x, y = road.pop(0)
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and arr[nx][ny] == '1':
            visited[nx][ny] = visited[x][y]+1
            road.append([nx, ny])