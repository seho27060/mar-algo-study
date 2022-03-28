n = int(input())
arr = list(map(int, input().split()))

sol = arr[0]
minV = 9999 * n
for i in range(n):
    sumV = 0
    for j in range(n):
        sumV += abs(arr[i] - arr[j])
    if minV > sumV or (minV == sumV and sol > arr[i]):
        minV = sumV
        sol = arr[i]
print(sol)

# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# print(arr[(n - 1) // 2])