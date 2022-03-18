def backtracking(get_,get_num):
    global k, min_,max_,lst
    if len(get_) == k+1:
        get_ = "".join(list(map(str,get_)))
        if int(min_) > int(get_):
            min_ = get_
        if int(max_) < int(get_):
            max_ = get_
        return
    else:
        for idx in range(len(get_num)):
            get_nxt = get_.copy()
            get_num2 = []
            if len(get_nxt) == 0:
                get_nxt.append(get_num[idx])
                get_num2 = get_num.copy()
                get_num2.pop(idx)
            else:
                if lst[len(get_nxt)-1] == "<":
                    if get_nxt[-1] < get_num[idx]:
                        get_nxt.append(get_num[idx])
                        get_num2 = get_num.copy()
                        get_num2.pop(idx)
                elif lst[len(get_nxt)-1] == ">":
                    if get_nxt[-1] > get_num[idx]:
                        get_nxt.append(get_num[idx])
                        get_num2 = get_num.copy()
                        get_num2.pop(idx)
            if get_num2 or len(get_nxt) == k+1:
                backtracking(get_nxt, get_num2)


num_lst = [i for i in range(10)]

k = int(input())
lst = input().split()
min_ = '9999999999'
max_ = '-1'
backtracking([],num_lst)
print(max_)
print(min_)
