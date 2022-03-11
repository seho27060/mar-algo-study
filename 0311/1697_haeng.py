N,K=map(int,input().split())
visited=[False for _ in range(100001)]

ST=[]                         #재귀로 런타임에러 몇대를 얻어맞고 와일문으로 풀었습니다.
visited[N] = True

ST.append([N,0])
cnt= 0
while ST:
    A=ST.pop(0)
    if A[0] == K:
        break
    for i in [A[0]*2,A[0]+1,A[0]-1]:
        if 0<=i<=100000 and visited[i] == False:
            ST.append([i,A[1]+1])
            visited[i]=True
print(A[1])