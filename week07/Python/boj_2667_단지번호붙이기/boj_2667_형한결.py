from collections import deque
n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
houses = []


drow = (0,0,-1,1)
dcol = (-1,1,0,0)


def bfs(graph:list,start:list)->int:
    graph[start[0]][start[1]] = '*'
    house_cnt = 1
    que = deque([start])
    while que:
        c_loc = que.popleft()
        for i in range(len(drow)):
            s_loc = [c_loc[0] + drow[i],c_loc[1] + dcol[i]]
            if s_loc[0]>=0 and s_loc[1]>=0 and s_loc[0]<n and s_loc[1]<n:
                if graph[s_loc[0]][s_loc[1]] == 1:
                    que.append(s_loc)
                    house_cnt = house_cnt + 1
                    graph[s_loc[0]][s_loc[1]] = '*'
    return house_cnt


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append(bfs(graph,start = [i,j]))


print(len(houses))
for i in sorted(houses):
    print(i)      
                    
                
                
            






