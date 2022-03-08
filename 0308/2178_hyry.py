import sys
input = sys.stdin.readline


def bfs(maze, N, M):
    Q = []
    visited = [[0] * M for _ in range(N)]

    Q.append((0, 0))
    visited[0][0] = 1

    while Q:
        currR, currC = Q.pop(0)
        if currR == N - 1 and currC == M - 1:
            return visited[currR][currC]

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR = currR + dr
            newC = currC + dc
            if 0 <= newR < N and 0 <= newC < M and\
                maze[newR][newC] == '1' and not visited[newR][newC]:
                Q.append((newR, newC))
                visited[newR][newC] = visited[currR][currC] + 1


N, M = map(int, input().split())
maze = [input() for _ in range(N)]

print(bfs(maze, N, M))

