import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
if sum(arr) < m:
    print(max(arr))
else:
    l, r = 0, max(arr)
    while l <= r:
        c = (l + r) // 2
        sumV = 0
        for i in arr:
            if i < c:
                sumV += i
            else:
                sumV += c
        if sumV <= m:
            l = c + 1
        elif sumV > m:
            r = c - 1
    print(r)