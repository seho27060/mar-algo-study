def bfs(start_):
    global bfs_visited
    ## 교재 코드 기반으로 구현.
    ## bfs는 층마다 너비따라 탐색
    queue = []
    queue.append(start_)
    while queue:
        get_ = queue.pop(0) ## 가장 먼저 삽입된 요소 pop
        if get_ not in bfs_visited:
            bfs_visited.append(get_)
        for i in lst[get_-1]: ## 이동한 노드에 연결된 간선을 따라 노드이동.
            if i not in bfs_visited: ## 노드를 방문하지 않았다면, 다음 탐색 경로 queue 추가, 방문기록 추가.
                queue.append(i)
                bfs_visited.append(i)

def dfs(start_): ## dfs 재귀로 구현
    global dfs_visited
    global lst

    if len(dfs_visited) == 0: ## 방문기록이 없다면 start_ 시작점 추가.
        dfs_visited.append(start_)
    for i in lst[start_-1]:   ## 깊이따라 탐색, 노드와 연결된 노드 순회
        if i not in dfs_visited: ## 순회하는 노드를 방문하지 않았다면,
            dfs_visited.append(i) ## 방문하고, dfs를 재귀적 실행.
            dfs(i)

n,m,v = map(int,input().split())
lst = [[] for k in range(n)] ## 간선 입력을 위한 리스트선언
                             ## idx번호 노드에 연결된 간선 추가.
for i in range(m):
    a,b = map(int,input().split())
    if b not in lst[a-1]:    ## 노드간 간선이 중복되어 입력될 수 있으므로,
        lst[a-1].append(b)   ## 간선은 양방향이므로, 불필요한 입력을 막기위해 조건문 삽입.
    if a not in lst[b-1]:    ## 굳이 리스트로 안하고 set으로 해도 되겠다.
        lst[b-1].append(a)
lst = list(map(sorted, lst)) ## dfs든 bfs든 탐색할때 애매하면 낮은 번호부터 탐색하므로, 이를 위해
                             ## 각 노드의 간선값에 대해 오름차순으로 정렬.
dfs_visited = []
bfs_visited = []
dfs(v)
bfs(v)
print(" ".join(str(x) for x in dfs_visited))
print(" ".join(list(map(str,bfs_visited))))


### 교재에서 나오는 방법.. dfs는 stack, bfs는 queue 사용.. 굳이 그럴 필요가없다..
###