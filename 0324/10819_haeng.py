def find(x):
    global result
    if x == N:
        sum_st=0
        for j in range(1,N):
            sum_st += abs(ST[j]-ST[j-1])
        if sum_st > result:
            result=sum_st
        return

    for i in range(N):
        if i in ST2:
            continue
        ST.append(A[i])
        ST2.append(i)
        find(x+1)
        ST.pop()
        ST2.pop()

N=int(input())
A=list(map(int,input().split()))

ST=[]
ST2=[]
result=0
find(0)
print(result)