import sys
T = int(sys.stdin.readline())

for _ in range(T):
    I = int(input())
    S = list(map(int, sys.stdin.readline().split()))
    E = list(map(int, sys.stdin.readline().split()))
    visited = [[False for _ in range(I)] for _ in range(I)]
    dx = [1,2,2,1,-1,-2,-2,-1]
    dy = [2,1,-1,-2,-2,-1,1,2]
    cnt = 0
    ST = [S+[cnt]]
    visited[S[1]][S[0]] = True
    while ST:
        s = ST.pop(0)
        cnt = s[-1]
        visited[s[1]][s[0]] = True
        if [s[0], s[1]] == E:
            break
        for i in range(8):
            nx = s[0] + dx[i]
            ny = s[1] + dy[i]
            if -1 < nx < I and -1 < ny < I and not visited[ny][nx]:
                ST.append([nx, ny, cnt + 1])
                visited[ny][nx] = True
    print(cnt)