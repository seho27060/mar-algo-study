import sys

sys.setrecursionlimit(10**9)

TC = int(input())

def dfs(i, j):
    if arr[i][j] == 0:
        return
    arr[i][j] = 0
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
            dfs(ni, nj)

for _ in range(TC):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
