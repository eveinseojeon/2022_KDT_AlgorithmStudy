from collections import deque

#! 0:통로 , 1:벽 , 2:출발 , 3:도착

drow = (1,-1,0,0)
dcol = (0,0,1,-1)

def bfs(graph:list,s:list)->int:
    que = deque([s])
    while que:
        c = que.popleft()
        for i in range(4):
            v = [c[0] + drow[i],c[1] + dcol[i]]
            if v[0] >=0 and v[0] <= N -1 and v[1] >=0 and v[1] <=N-1:
                if graph[v[0]][v[1]] == 3:
                    return int(graph[c[0]][c[1]]/2 -1)
                    break
                    que = False
                elif graph[v[0]][v[1]] == 0:
                    que.append(v)
                    graph[v[0]][v[1]]= graph[c[0]][c[1]] +2            
    return 0         
                
                
    



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                _s = [i,j]
    print(f"#{test_case} {bfs(graph,_s)}")
            
            