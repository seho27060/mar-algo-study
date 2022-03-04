TC = int(input())

def bfs(i, j):
    visited = [[0] * l for _ in range(l)]
    q = []
    q.append([i, j])
    visited[i][j] = 0
    while q:
        i, j = q.pop(0)
        if i == end[0] and j == end[1]:
            return visited[i][j]
        for di, dj in [[1, 2], [2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < l and 0 <= nj < l and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1

for _ in range(TC):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    arr = [[0] * l for _ in range(l)]
    minV = bfs(start[0], start[1])
    print(minV)

