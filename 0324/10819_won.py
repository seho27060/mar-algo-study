n = int(input())

ARR = list(map(int, input().split()))
v = [False] * n

def f(i, arr):
    global maxV
    if i == n:
        sumV = 0
        for j in range(n - 1):
            sumV += abs(arr[j] - arr[j + 1])
        if maxV < sumV:
            maxV = sumV
        return
    for j in range(n):
        if not v[j]:
            v[j] = True
            f(i + 1, arr + [ARR[j]])
            v[j] = False
maxV = 0
f(0, [])
print(maxV)