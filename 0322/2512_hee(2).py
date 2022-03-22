# 이진탐색

import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

def binary(start, end):
    if end < start:
        return end

    mid = (start + end) // 2
    temp = 0
    for i in lst:
        if mid >= i:
            temp += i
        else:
            temp += mid

    if temp == M:
        return mid
    if temp < M:
        return binary(mid+1, end)
    else:
        return binary(start, mid -1)

print(binary(0, max(lst)))
