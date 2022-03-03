import sys
sys.setrecursionlimit(10**9)

T= int(input())
for t in range(T):
    M,N,K = map(int, input().split())
    Nlist=[[0]*M for _ in range(N)]
    for i in range(K):
        a,b=map(int,input().split())
        Nlist[b][a] = 1


    visited=[[False]*M for _ in range(N)]
    ST=[]
    def BFS(x1,y1):
        visited[y1][x1]=True
        dx = [1, -1, 0, 0]
        dy = [0,0,1,-1]
        for j in range(4):                      #해당 좌표 상하좌우 확인
            A = x1 + dx[j]
            B = y1 + dy[j]
            if 0<=A<M and 0<=B<N and Nlist[B][A] == 1 and visited[B][A] == False:
                ST.append(A)
                ST.append(B)                #상하좌우좌표가 범위에 있을경우 좌표 추가
        while ST:
            x2 = ST.pop(0)                  #ST에 좌표가 있을경우 불러와서 다시확인
            y2 = ST.pop(0)
            if visited[y2][x2] == False:
                BFS(x2,y2)


    cnt=0
    for y in range(N):                      # 좌표 확인하면서 카운트하고 해당값을 BFS
        for x in range(M):
            if Nlist[y][x] == 1 and visited[y][x] == False:
                cnt +=1
                BFS(x,y)
    print(cnt)