N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[3], reverse=True)
arr.sort(key=lambda x: x[2], reverse=True)
arr.sort(key=lambda x: x[1], reverse=True)
ans = 1
R = arr[0][1:]
    if arr[i][1:] == R:
        pass
    else:
        R = arr[i][1:]
        ans = i+1
    if arr[i][0] == K:
        print(ans)
        break
for i in range(N):

