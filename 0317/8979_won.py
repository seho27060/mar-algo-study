n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

arr = sorted(arr, key=lambda x: (-x[1], -x[2], -x[3]))
# print(arr)
tmp = 0
for i in range(n):
    if arr[i][0] == k:
        tmp = i
# print(tmp)

sol = 0
for i in range(n):
    if arr[i][1:] == arr[tmp][1:]:
        sol = i
        break

print(sol + 1)