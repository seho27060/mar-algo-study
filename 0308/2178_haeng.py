N,M=map(int,input().split())
Nlist=[]
for _ in range(N):
    Nlist.append(input())

visited = [[False]*M for _ in range(N)]

ST=[]
A=[0,0,1]
visited[0][0]=True

while 1:
    if A[0] == M-1 and A[1] == N-1:
        print(A[2])
        break
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    cnt = A[2]+1
    for i in range(4):
        X = A[0] + dx[i]
        Y = A[1]  + dy[i]
        if 0<=X<M and 0<=Y<N and Nlist[Y][X] == '1' and visited[Y][X] == False:
            ST.append([X, Y, cnt])
            visited[Y][X] = True
    A=ST.pop(0)