import sys
input = sys.stdin.readline

# 재귀
# sys.setrecursionlimit(10 ** 9)를 써보자

# def popout(fields, row, col, N, M):
#     fields[row][col] = 0
#
#     for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#         newR = row + dr
#         newC = col + dc
#         if 0 <= newR < N and 0 <= newC < M and fields[newR][newC] == 1:
#             popout(fields, newR, newC, N, M)

# stack
def popout(fields, row, col, N, M):
    ST = [(row, col)]
    fields[row][col] = 0
    # visited 쓰지 않고 지나간 곳은 0으로 마크

    while ST:
        currR, currC = ST.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR = currR + dr
            newC = currC + dc
            if 0 <= newR < N and 0 <= newC < M and fields[newR][newC] == 1:
                ST.append((newR, newC))
                fields[newR][newC] = 0

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    fields = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        fields[Y][X] = 1

    worms = 0
    for row in range(N):
        for col in range(M):
            if fields[row][col] == 1:
                popout(fields, row, col, N, M)
                # 배추 다 뽑아서 0으로 만들면
                # 배추 구역 하나 다 봤으니 벌레 += 1
                worms += 1

    print(worms)