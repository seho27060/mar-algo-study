import sys
## 매개변수...탐색..
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
max_ = max(lst)
min_ = 0

while min_ <=  max_:
    result = 0
    mid_ = (max_ + min_) // 2
    for get_ in lst:
        if get_ < mid_:
            result += get_
        else:
            result += mid_
    if result <= m:
        min_ = mid_+1
    elif result > m:
        max_ = mid_-1
print(max_)