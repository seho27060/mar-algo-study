n = int(input())
m = int(input())
stu = list(map(int, input().split()))
photo = []
cnt = []
for i in range(m):
    if len(photo) < n and stu[i] not in photo:
        photo.append(stu[i])
        cnt.append(1)
    elif len(photo) < n and stu[i] in photo:
        cnt[photo.index(stu[i])] += 1
    elif len(photo) >= n and stu[i] in photo:
        idx = photo.index(stu[i])
        cnt[idx] += 1
    else:
        x = min(cnt)
        y = cnt.count(x)
        if y == 1:
            photo[cnt.index(x)] = stu[i]
            cnt[cnt.index(x)] = 1
        else:
            del photo[cnt.index(x)]
            del cnt[cnt.index(x)]
            photo.append(stu[i])
            cnt.append(1)
photo.sort()
print(*photo)