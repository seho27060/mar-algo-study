N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

D = [(-1, 0), (1, 0), (0, 1), (0, -1)]
num = N*N
H = 1
cnt = 1
while num:
    # 침수
    for i in range(N):
        for j in range(N):
            if A[j][i] == H:
                A[j][i] = -1
                num -= 1
    # DFS를 이용한 안전한 영역 갯수 체크
    temp_cnt = 0
    V = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[j][i] != -1 and not V[j][i]:
                temp_cnt += 1
                ST = [(i, j)]
                V[j][i] = True
                while ST:
                    x, y = ST.pop()
                    for d in D:
                        nx = x + d[0]
                        ny = y + d[1]
                        if -1 < nx < N and -1 < ny < N and A[ny][nx] != -1 and not V[ny][nx]:
                            V[ny][nx] = True
                            ST.append((nx, ny))
    cnt = max(cnt, temp_cnt)
    H += 1
print(cnt)