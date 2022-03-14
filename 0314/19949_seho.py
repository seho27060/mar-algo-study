def makeanswer(get_,score):
    global lst, result
    ## 해당 재귀에서 다음칸에 넣을 답 번호들.
    num_lst = [1,2,3,4,5]

    ## 만약 get_의 길이가 10이상이라면, 점수확인을 한다.
    if len(get_) >= 10:
        ## score가 5이상이라면
        if score >= 5:
            ## result에 1 더해준다.
            result += 1
        return
    else:
        ## get_의 길이가 2이상이라면, 마지막 답과 그 전 답의 일치를 확인.
        if len(get_) >= 2:
            ## 일치한다면, 다음 칸에 넣을 번호 후보중, 연속되는 번호를 삭제.
            if get_[-1] == get_[-2]:
                num_lst.pop(get_[-1]-1)

        ## 다음 칸에 넣을 번호 num_lst 순회.
        for nxt in num_lst:
            ## 복사하고 붙여넣기로 backtracking
            get_2 = get_.copy()
            get_2.append(nxt)
            score_2 = score
            ## 넣은 번호가 실제 답안의 답과 같다면, score_2 1추가.
            if get_2[len(get_2)-1] == lst[len(get_2)-1]:
                score_2 += 1
            ## 재귀 실행.
            makeanswer(get_2,score_2)
## 답 비교를 위한 10개 답안 입력
lst = list(map(int,input().split()))

result = 0
answer = []
## 빈리스트, 맞은갯수로 backtracking 시작.
makeanswer(answer,0)
print(result)

