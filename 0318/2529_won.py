n = int(input())

ARR = input().split()

def f(i, arr):
    global minV, maxV, minSol, maxSol
    if i == n + 1:
        flag = True
        for j in range(len(ARR)):
            if ARR[j] == '<':
                if arr[j] > arr[j + 1]:
                    flag = False
            elif ARR[j] == '>':
                if arr[j] < arr[j + 1]:
                    flag = False
        if flag:
            tmp = 0
            for j in range(n + 1):
                tmp += arr[j] * (10 ** (n - j))
            # print(arr, tmp)
            if minV > tmp:
                minV = tmp
                minSol = ''.join(map(str, arr))
            if maxV < tmp:
                maxV = tmp
                maxSol = ''.join(map(str, arr))
        return
    for j in range(10):
        if not visited[j]:
            if not arr:
                visited[j] = True
                f(i + 1, arr + [j])
                visited[j] = False
            else:
                if ARR[len(arr) - 1] == '<' and arr[-1] < j:
                    visited[j] = True
                    f(i + 1, arr + [j])
                    visited[j] = False
                elif ARR[len(arr) - 1] == '>' and arr[-1] > j:
                    visited[j] = True
                    f(i + 1, arr + [j])
                    visited[j] = False

visited = [False] * 10
minV = 10 ** (n + 1)
maxV = 0
minSol = ''
maxSol = ''
f(0, [])
print(maxSol)
print(minSol)
