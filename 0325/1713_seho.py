from collections import deque
n = int(input())
recommend = int(input())
lst = list(map(int,input().split()))
picture = []

for idx in range(recommend):
    if len(picture) < n:
        check = True
        for find_num in range(len(picture)):
            if picture[find_num][0] == lst[idx]:
                picture[find_num][1] += 1
                check = False
                break
        if check:
            picture.append([lst[idx],1,idx])
    else:
        ## 번호ㅡ 추천개수 시간(인덱스)
        check = True
        for find_num in range(len(picture)):
            if picture[find_num][0] == lst[idx]:
                picture[find_num][1] += 1
                check = False
                break
        if check:
            picture.sort(key=lambda x:(x[1],x[2]),reverse=True)
            picture.pop()
            picture.append([lst[idx],1,idx])
answer = []
for ans in picture:
    answer.append(ans[0])
answer.sort()
print(*answer)