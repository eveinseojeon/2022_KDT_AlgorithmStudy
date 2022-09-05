from collections import deque

def bfs(start_loc:list,graph:list):
    goal = 0
    que = deque([start_loc])
    d_row = (-1,1,0,0)
    d_col = (0,0,-1,1)
    while que:
        current_loc = que.popleft()
        for i in range(4):
            search_loc = [current_loc[0]+d_row[i],current_loc[1]+d_col[i]]
            if search_loc[0]>=0 and search_loc[1]>=0 and search_loc[0]<=N-1  and search_loc[1]<=N-1:
                if graph[search_loc[0]][search_loc[1]]==0:
                    graph[search_loc[0]][search_loc[1]] = '*'
                    que.append(search_loc)
                elif  graph[search_loc[0]][search_loc[1]] ==3:
                    goal = 1
                    que = False
                    break
    
    return goal


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if graph[row][col]==2:
                break
    start_loc = [row,col]    

    print(f'#{test_case} {bfs(start_loc,graph)}')


    