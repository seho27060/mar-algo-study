N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(input()))
visited = [[False] * M for _ in range(N)]

S = [0, 0, 1]
E = [M-1, N-1]
ST = [S]
visited[S[1]][S[0]] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while ST: # bfs
    s = ST.pop(0)
    if s[0:2] == E:
        break
    for i in range(4):
        nx = s[0] + dx[i]
        ny = s[1] + dy[i]
        if -1 < nx < M and -1 < ny < N and maze[ny][nx] == '1' and not visited[ny][nx]:
            ST.append([nx, ny, s[-1]+1])
            visited[ny][nx] = True
print(s[-1])


