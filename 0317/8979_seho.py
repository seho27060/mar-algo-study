# 나라개수, 등수가 알고싶은 국가 k
n, k = map(int,input().split())

# 나라이름 금 은 동
lst = [list(map(int,input().split())) for _ in range(n)]
lst = sorted(lst, key= lambda x: x[1:], reverse = True)
# print(lst)
rank = 1
rankb = 0
if lst[0][0] == k:
    print(lst[0][0])
else:
    for get_ in range(1,len(lst)):
        rankb += 1
        if lst[get_-1][1] != lst[get_][1]:
            rank += rankb
            rankb = 0
        else:
            if lst[get_-1][2] != lst[get_][2]:
                rank += rankb
                rankb = 0
            else:
                if lst[get_-1][3] != lst[get_][3]:
                    rank += rankb
                    rankb = 0
        # print(rank,rankb)
        if lst[get_][0] == k:
            if lst[get_-1][1] == lst[get_][1] and lst[get_-1][2] == lst[get_][2] and lst[get_-1][3] == lst[get_][3]:
                print(rank)
            else:
                print(rank + rankb)
            break
