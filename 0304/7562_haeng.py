T = int(input())
for t in range(T):
    l = int(input())
    a,b=map(int,input().split())
    c,d=map(int,input().split())

    NN= [[0]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]                        #재귀 사용할때 오류를 못고쳐서 와일문으로 교체했습니다.

    dx = [-2, -1, -2, -1, 1, 2, 1, 2]
    dy = [-1, -2, 1, 2, -2, -1, 2, 1]
    ST=[]
    cnt=0


    while 1:
        visited[b][a] = True
        if a == c and b == d:                                      #a,b가 c,d값이 될 경우 cnt를 저장
            result = cnt
            break
        cnt+=1                                                     # cnt 1번증가
        for i in range(8):
            X=a+dx[i]                                              #해당 위치에서 이동가능한 위치와 현재 cnt를 ST에 저장
            Y=b+dy[i]
            if 0<=X<l and 0<=Y<l and visited[Y][X]==False:
                visited[Y][X] = True
                ST.append([X,Y,cnt])
        if ST:                                                     #ST값을 앞에서부터 불러와서 반복
            A=ST.pop(0)
            a=A[0]
            b=A[1]
            cnt=A[2]

    print(result)