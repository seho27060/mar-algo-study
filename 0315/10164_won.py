import sys
input = sys.stdin.readline

n, m, k = map(int, input().strip().split())
arr = [[0] * m for _ in range(n)]

if k == 0:
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    print(arr[n - 1][m - 1])
else:
    ci = (k - 1) // m
    cj = (k - 1) % m

    for i in range(ci + 1):
        for j in range(cj + 1):
            if i == 0 or j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    tmp = arr[ci][cj]

    for i in range(ci, n):
        for j in range(cj, m):
            if i == ci or j == cj:
                arr[i][j] = tmp
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
    print(arr[n - 1][m - 1])
