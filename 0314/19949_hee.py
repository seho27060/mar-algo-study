ans = list(map(int, input().split()))
result = 0

def solve(idx, cnt, before_ans, score):
    if cnt == 3:
        return
    if idx == 10:
        if score >= 5:
            global result
            result += 1
        return

    for i in range(1,6):
        if ans[idx] == i and before_ans == i:
            solve(idx+1, cnt+1, i, score+1)
        elif ans[idx] == i:
            solve(idx+1, 1, i, score+1)
        elif before_ans == i:
            solve(idx+1, cnt+1, i, score)
        else:
            solve(idx+1, 1, i, score)

solve(0, 0, -1, 0)
print(result)
