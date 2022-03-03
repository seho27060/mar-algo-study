T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    G = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        G[y][x] = 1
    # graph 생성
    visited = [[False for _ in range(M)] for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # delta 초기화 : right, left, up, down

    ST = []
    cnt = 0
    for x in range(M):
        for y in range(N):
            # 배추가 없거나 이미 방문한 곳은 pass
            if G[y][x] == 0 or visited[y][x]:
                continue
            cnt += 1
            ST.append([x, y])
            # 이웃한 배추 모두 방문 처리
            while ST:
                s = ST.pop(0)
                visited[s[1]][s[0]] = True
                for i in range(4):
                    nx = s[0] + dx[i]
                    ny = s[1] + dy[i]
                    if -1 < nx < M and -1 < ny < N and not visited[ny][nx] and G[ny][nx] == 1:
                        ST.append([nx, ny])
                while ST and visited[ST[0][1]][ST[0][0]]:
                    ST.pop(0)
    print(cnt)