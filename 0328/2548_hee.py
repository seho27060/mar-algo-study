import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr_set = set(arr)
ans = 10**9
min_val = 10**9
for i in arr_set:
    val = 0
    for j in arr:
        val += abs(i-j)
        if val > min_val:
            break
    if min_val >= val:
        if min_val == val:
            ans = min(i, ans)
        else:
            ans = i
        min_val = val
print(ans)
