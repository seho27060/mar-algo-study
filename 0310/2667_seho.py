def dfs(start_):
    global lst,n
    ## 단지는 상하좌우로 연결되니까 delta 설정
    delta = [(1,0),(-1,0),(0,1),(0,-1)]
    stack = [start_]
    count = 0
    while stack:
        tmp = stack.pop()
        ## 현재 좌표 확인, 해당 좌표가 1이면 0으로 바꾸고 count 증가
        if lst[tmp[0]][tmp[1]] == '1':
            lst[tmp[0]][tmp[1]] = '0'
            count += 1
        ## 해당좌표에서 상하좌우로 1이면 이동으로 추가. 블라블라
        for move in delta:
            row = tmp[0] + move[0]
            col = tmp[1] + move[1]
            if (0 <= row < n and 0 <= col < n) and (lst[row][col] == '1'):
                stack.append([row,col])
    ## 단지내의 아파트 개수 반환
    return count


n = int(input())

lst = [list(input()) for _ in range(n)]

answer = []

## 전체 좌표를 탐색.
for row in range(n):
    for col in range(n):
        ## 좌표에서 1을 만나면
        if lst[row][col] == "1":
            ## 좌표(row,col)에서 아파트 단지를 탐색하는 dfs 실행
            answer.append(dfs([row,col]))
            ## answer에 반환값 추가.

print(len(answer))
## answer을 오름차순으로 출력해야하니,, sort안쓰고 정렬할 방법이 있을까?
answer.sort()
for out_ in answer:
    print(out_)
