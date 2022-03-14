def score(lst, n, s):
    global cnt
    if n == 10:
        if s>=5:
            cnt += 1
        return
    if s<5 and lst.count(0)<5-s:
        return
    for i in range(1, 6):
        if n>1 and lst[n-1]==i and lst[n-2]==i:
            continue
        lst[n] = i
        if ans[n] == lst[n]:
            score(lst, n+1, s+1)
        else:
            score(lst, n+1, s)
        lst[n] = 0

ans = list(map(int, input().split()))
lst = [0]*10
cnt = 0
score(lst, 0, 0)
print(cnt)