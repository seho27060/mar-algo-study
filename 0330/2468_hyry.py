import sys
input = sys.stdin.readline


def safePlace(row, col, rain):
    ST = [(row, col)]
    visited[row][col] = True

    while ST:
        currR, currC = ST.pop()

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR = currR + dr
            newC = currC + dc
            if 0 <= newR < N and 0 <= newC < N and\
                    not visited[newR][newC] and area[newR][newC] > rain:
                ST.append((newR, newC))
                visited[newR][newC] = True


N = int(input())
area = []
rains = {0}
for _ in range(N):
    a = list(map(int, input().split()))
    area.append(a)
    rains.update(a)

maxCnt = 0
for rain in rains:
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if not visited[row][col] and area[row][col] > rain:
                safePlace(row, col, rain)
                cnt += 1
    if maxCnt < cnt:
        maxCnt = cnt

print(maxCnt)
