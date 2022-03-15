# 중학교 때 길찾기 

# N은 행, M은 열, K는 0일 수도 아닐 수도
N, M, K = map(int, input().split())

land = [[0] * M for _ in range(N)]

if K == 0:
    for row in range(N):
        land[row][0] = 1
    for col in range(M):
        land[0][col] = 1

    for row in range(1, N):
        for col in range(1, M):
            land[row][col] = land[row - 1][col] + land[row][col - 1]

    print(land[N - 1][M - 1])

else:
    # k의 행 구하기
    k_row = K // M
    if K % M == 0:
        k_row -= 1
    # k의 열 구하기
    k_col = K % M - 1
    if K % M == 0:
        k_col = M - 1

    # 사각형1
    for row in range(k_row + 1):
        land[row][0] = 1
    for col in range(k_col + 1):
        land[0][col] = 1

    for row in range(1, k_row + 1):
        for col in range(1, k_col + 1):
            land[row][col] = land[row - 1][col] + land[row][col - 1]

    # 사각형2
    for row in range(k_row, N):
        land[row][k_col] = land[k_row][k_col]
    for col in range(k_col, M):
        land[k_row][col] = land[k_row][k_col]

    for row in range(k_row + 1, N):
        for col in range(k_col + 1, M):
            land[row][col] = land[row - 1][col] + land[row][col - 1]

    print(land[N - 1][M - 1])