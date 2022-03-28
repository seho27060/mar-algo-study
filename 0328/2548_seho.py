n = int(input())
lst = list(map(int,input().split()))
lstSet = sorted(set(lst))
minSum = float("inf")
minNum = 10001
for idx in range(len(lstSet)):
    getSum = 0
    for lstIdx in range(len(lst)):
        if lstSet[idx] != lst[lstIdx]:
            getSum += abs(lstSet[idx] - lst[lstIdx])
    if minSum >= getSum:
        if minSum == getSum:
            minNum = min(lstSet[idx],minNum)
        else:
            minNum = lstSet[idx]
        minSum = getSum
print(minNum)