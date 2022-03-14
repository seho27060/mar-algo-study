import sys
input = sys.stdin.readline

def f(i, s):
    global sol
    if i == n:
        if s >= 5:
            sol += 1
    elif s + n - i < 5:
        return
    else:
        for j in range(1, 6):
            if bit[i - 2] == bit[i - 1] and j == bit[i - 2]:
                continue
            bit[i] = j
            if bit[i] == arr[i]:
                f(i + 1, s + 1)
            else:
                f(i + 1, s)

arr = list(map(int, input().strip().split()))
arr = [0, 0] + arr
n = len(arr)
bit = [0] * n
sol = 0
f(2, 0)
print(sol)
