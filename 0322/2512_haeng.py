N=int(input())
Nlist=list(map(int,input().split()))
M=int(input())

A=max(Nlist)
while sum(Nlist)>M:
    for i in range(N):
        if Nlist[i]== A:
            Nlist[i] -= 1
    A -= 1
print(A)