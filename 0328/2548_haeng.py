N=int(input())
Nlist=sorted(list(map(int,input().split())))

Y = [0,99999999999]
for i in Nlist:
    sumN=0
    for j in Nlist:
        sumN += abs(i-j)
    if sumN < Y[1]:
        Y = [i,sumN]

print(Y[0])