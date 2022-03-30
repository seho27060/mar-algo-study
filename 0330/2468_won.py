import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())  # n x n
arr = [list(map(int, input().split())) for _ in range(n)]
sol = 0
def f(si, sj, c):
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = si + di, sj + dj
        if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0 and sink[ni][nj] == 1:
            v[ni][nj] = c
            f(ni, nj, c)

for h in range(101):
    sink = [[0] * n for _ in range(n)]  # 0이면 잠김, 1이면 안잠김
    v = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h:
                sink[i][j] = 1
    for i in range(n):
        for j in range(n):
            if sink[i][j] == 1 and v[i][j] == 0:
                cnt += 1
                f(i, j, cnt)
                if sol < cnt:
                    sol = cnt
print(sol)
