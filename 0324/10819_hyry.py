def findMax(depth, curS):
    global maxS

    if depth == N:
        if maxS < curS:
            maxS = curS
    else:
        for idx in range(len(arr)):
            if not used[idx]:
                result[depth] = arr[idx]
                used[idx] = True
                if depth != 0:
                    findMax(depth + 1, curS + abs(result[depth - 1] - result[depth]))
                else:
                    findMax(depth + 1, curS)
                used[idx] = False


N = int(input())
arr = list(map(int, input().split()))
used = [False] * N
result = [1000] * N
maxS = -1e10
findMax(0, 0)
print(maxS)
