import sys
input = sys.stdin.readline

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True

def f(i, arr):
    if i == n:
        if len(arr) == m:
            tmp = sum(arr)
            if isPrime(tmp) and sol.count(tmp) == 0:
                sol.append(tmp)
        return
    if len(arr) > m:
        return
    arr.append(inputArr[i])
    f(i + 1, arr)
    arr.pop()
    f(i + 1, arr)

n, m = map(int, input().strip().split())
inputArr = list(map(int, input().strip().split()))
sol = []
f(0, [])
if not sol:
    print(-1)
else:
    sol.sort()
    print(*sol)
