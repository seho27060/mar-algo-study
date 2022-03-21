def MakeWorkingOutPlan(get_weight,get_plan):
    global k,result
    ## 순서있는, 중복없는 순열만들기.
    ## 재귀적으로 구현
    ## 값을 대입하고 weight 조건을 따졌을때, 계속 만들지 중단할지 결정.
    if get_plan:

        for get_ in range(len(get_plan)):
            nxt_weight = get_weight - k
            nxt_plan = get_plan.copy()
            nxt_weight += nxt_plan.pop(get_)
            if nxt_weight >= 500:
                MakeWorkingOutPlan(nxt_weight,nxt_plan)
    else:
        if get_weight >= 500:
            result += 1

## 순서가 있는, 중복없는 순열을 생성.
## 요소가 추가될때 마다 weight에 대한 조건식 검증
## 순열 완성까지 weight 조건을 만족하면 result 1 추가.
weight = 500
n,k = map(int,input().split())
WorkingOutKits = list(map(int,input().split()))
result = 0
MakeWorkingOutPlan(weight,WorkingOutKits)
print(result)
