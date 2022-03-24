def make_sum(get_lst):
    result = 0

    for idx in range(len(get_lst)-1):
        result += abs(get_lst[idx]-get_lst[idx+1])
    return result

def makePm(output,get_,n):
    if len(output) == n:
        global answer
        answer.append(make_sum(output))
    else:
        for idx in range(len(get_)):
            get_2 = get_.copy()
            nxtout = output.copy()

            nxtout.append(get_2.pop(idx))
            makePm(nxtout,get_2,n)
n = int(input())
lst = list(map(int,input().split()))
answer = []
makePm([],lst,n)
print(max(answer))