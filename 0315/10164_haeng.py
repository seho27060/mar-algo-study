N,M,K=map(int,input().split())
Nlist=[[] for _ in range(N)]
a=1
for i in range(N):
    for j in range(M):
        Nlist[i].append(a)
        if a == K:
            KK=[i,j]
        a += 1
if K == 0:
    for i in range(N):
        for j in range(M):
            if i==0 or j == 0:
                Nlist[i][j] = 1
            else:
                Nlist[i][j] = Nlist[i - 1][j] + Nlist[i][j - 1]
    print(Nlist[N-1][M-1])

else:
    for i in range(KK[0]+1):
        for j in range(KK[1]+1):
            if i==0 or j == 0:
                Nlist[i][j] = 1
            else:
                Nlist[i][j] = Nlist[i - 1][j] + Nlist[i][j - 1]
    A=Nlist[KK[0]][KK[1]]

    for i in range(KK[0],N):
        for j in range(KK[1],M):
            if i==KK[0] or j == KK[1]:
                Nlist[i][j] = 1
            else:
                Nlist[i][j] = Nlist[i - 1][j] + Nlist[i][j - 1]
    B=Nlist[N-1][M-1]

    print(A*B)