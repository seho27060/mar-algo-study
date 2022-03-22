n = int(input())
b = list(map(int, input().split()))
m = int(input())
l, r = 0, max(b)

if sum(b) <= m:
    print(max(b))
else:
    while l <= r:
        mid = (l+r)//2
        total = 0
        for bb in b:
            total += min(mid, bb)
        if total>m:
            r = mid-1
        else:
            l = mid+1
    print(r)