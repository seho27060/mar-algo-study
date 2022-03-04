def bfs(start_ ,count):
    global answer
    global end_
    global n
    global visited

    find_lst = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]] ## 8방향에 이동을 위한 델타.
    queue = []
    count += 1  ## 이동거리

    for i in start_: ## start_ 리스트 순회. 탐색 기준이 될 좌표들. for 문을 통해 queue로 구현.
        for j in find_lst:  ## 기준 좌표에 델타로 이동
            x = i[0] + j[0]
            y = i[1] + j[1]
            if (0 <= x < n and 0 <= y < n): ## 이동한 좌표가 범위 내에 있다면,
                if visited[y][x] == 0:      ## 이동한 좌표를 방문하지 않았다면,
                    if x == end_[0] and y == end_[1]:   ## 방문좌표가 도착점이라면
                        answer = count                  ## 답에 이동거리를 할당. 재귀 중단.
                        return
                    else:
                        visited[y][x] = count           ## 아니라면 해당 좌표에 이동거리를 할당.
                        queue.append([x,y])             ## 다음 탐색기준이 될 리스트에 추가한다.
                else:
                    visited[y][x] = count  ## 방문했다면, 현재 거리로 갱신. * 거리 비교를 하고 작은 값으로 갱신해야한다. 잘못된 부분.

    if queue:  ## 다음 탐색 기준이 될 좌표가 있다면,
        bfs(queue,count) ## bfs 재귀적 실행.
    else:
        return ## 없다면 재귀 종료.

## 도착점까지의 최단거리 구하기.

nums = int(input())

for i in range(nums):
    n = int(input())
    start_ = list(map(int,input().split()))
    end_ = list(map(int,input().split()))

    visited = [[0]*n for _ in range(n)] ## 방문 리스트 형성
    visited[start_[1]][start_[0]] = 1   ## 시작점은 1로 초기화
    answer = 0    ## 이동거리 0으로 초기화
    bfs([start_],0) ## bfs 실행.
    print(answer)