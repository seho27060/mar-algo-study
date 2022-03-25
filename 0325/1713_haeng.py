N=int(input())
cnt=int(input())
Nlist=list(map(int,input().split()))

ST=[]   #학생번호
ST2=[]  #추천수
ST3=[]  #들어온날짜

for p in range(cnt):
    if Nlist[p] in ST:
        for j in range(len(ST)):
            if ST[j] == Nlist[p]:
                ST2[j] += 1

    else:
        if len(ST) < N:
            ST.append(Nlist[p])
            ST2.append(1)
            ST3.append(p)

        else:
            A = [min(ST2),N+1,cnt+1]
            for i in range(N):
                if ST2[i] == A[0] and ST3[i] < A[2]:
                    A = [A[0],i,ST3[i]]
            ST[A[1]] = Nlist[p]
            ST2[A[1]] = 1
            ST3[A[1]] = p
ST.sort()
print(*ST)