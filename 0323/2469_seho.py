k = int(input())
n = int(input())

lst = list(input())
## 처음 알파벳들의 시작 위치, idx == 알파벳
start_lst = sorted(lst)
## 알파벳들의 도착 위치, idx == 알파벳
end_lst = []
for alpha in start_lst:
    for end_ in range(len(lst)):
        if lst[end_] == alpha:
            end_lst.append(end_)
            break
# print(end_lst)

ladder = [list(input()) for _ in range(n)]
questionloc = 0
for loc in range(n):
    if "?" in ladder[loc]:
        questionloc = loc
        ladder[loc] = list("*"*(k-1))

# for kk in ladder:
#     print(kk)
## start_lst에서 아래로 내려가서 questionloc 에서 위치 a확인
## lst기준으로 아래에서 위로 올라가면서 questionloc에서 위치 b확인

## 위에서 아래로 qloc 까지 이동, 거기서 a 구하기
a_lst = []
# print(start_lst)
# print([_ for _ in range(len(start_lst))])
for start_loc in range(len(start_lst)):
    now_ = start_loc
    for row in range(0,questionloc):
        if now_ == 0:
            if ladder[row][now_] == "-":
                now_ += 1
        elif now_ == (k-1):
            if ladder[row][now_-1] == "-":
                now_ -= 1
        else:
            if ladder[row][now_-1] == "-":
                now_ -= 1
            elif ladder[row][now_] == "-":
                now_ += 1
    a_lst.append(now_)
# print(a_lst)
## 아래에서 위로 qloc까지 이동 b 찾기
b_lst = []
for end_loc in end_lst:
    now_ = end_loc
    for row in range(n-1,questionloc,-1):
        if now_ == 0:
            if ladder[row][now_] == "-":
                now_ += 1
        elif now_ == (k-1):
            if ladder[row][now_-1] == "-":
                now_ -= 1
        else:
            if ladder[row][now_-1] == "-":
                now_ -= 1
            elif ladder[row][now_] == "-":
                now_ += 1
    b_lst.append(now_)
# print(b_lst)
# print(end_lst)
# print(list("ACGBEDJFIH"))
## a - b == 1 이면 b에 - 대입
## abs(a-b) > 1 이면 x
## a - b == -1 이면 a에 - 대입
## 그외라면 *대입
new_ladder = ["*"]*(k-1)
check = True
for get_ in range(k):
    if abs(a_lst[get_] - b_lst[get_]) > 1:
        check = False
        break
    elif a_lst[get_] - b_lst[get_] == 1:
        new_ladder[b_lst[get_]] = "-"
    elif a_lst[get_] - b_lst[get_] == -1:
        new_ladder[a_lst[get_]] = "-"
if check:
    print("".join(new_ladder))
else:
    print("x"*(k-1))

