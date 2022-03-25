n = int(input())  # 3
l = int(input())  # 9
arr = list(map(int, input().split()))
pic = []
rec = []

for i in range(l):
    for j in range(len(pic)):
        if pic[j] == arr[i]:
            rec[j] += 1
            break
    else:
        if len(pic) >= n:
            minK = 0
            for k in range(n):
                if rec[minK] > rec[k]:
                    minK = k
            pic.pop(minK)
            rec.pop(minK)
        pic.append(arr[i])
        rec.append(1)
pic.sort()
print(*pic)
