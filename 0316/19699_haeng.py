N,M = map(int,input().split())
Nlist = list(map(int, input().split()))

Mlist=[]
Mlist2 = []
result=[]

def sonanda(x):                             # 개수가 M개인 부분집합찾기
    global I
    if x == M:
        A=sum(Mlist)
        cnt =0
        for i in range(1,A+1):              #찾았을때 합한값이 소수인지 체크
            if A%i==0:
                cnt +=1
        if cnt==2 and A not in result:
            result.append(A)
        return

    if Mlist:
        for i in range(I+1,N):
            if i in Mlist2:
                continue
            Mlist.append(Nlist[i])           # 중복된 값 안들어가게 Mlist2에 인덱스값 저장
            Mlist2.append(i)
            I = i
            sonanda(x + 1)
            Mlist.pop()
            Mlist2.pop()

    else:
        for i in range(0,N-M+1):
            Mlist.append(Nlist[i])
            Mlist2.append(i)
            I = i
            sonanda(x+1)
            Mlist.pop()
            Mlist2.pop()

sonanda(0)
result.sort()

if result:
    print(*result)
else:
    print(-1)