from collections import deque


drow = (1,-1,0,0)
dcol = (0,0,1,-1)

m,n  = map(int,input().split())


graph = [list(map(int,input().split())) for _ in range(n)]


good = {}
dont = False
# 익은 토마토 위치를 키로, 해당 val은 que로 저장

for i in range(n):
    if 0 in graph[i]: 
        dont = True # 모두 0이면 할 필요가 없음, 모두-1인 상황 X
    for j in range(m):
        if graph[i][j]  == 1:
            good[(i,j)] = deque([[i,j]])

# 각 que들의 개수를 계산하는 함수
def sum_func(good):
    que_sum = 0
    for value in good:
        que_sum  = que_sum + len(good[value])
        return que_sum


def bfs(good,graph):
    # 각 que의 길이가 0이면 종료
    while sum_func(good)!=0:
        for tomato in good: #각 start 지점
            if len(good[tomato]) !=0:
                current = good[tomato].popleft()
                for  i in range(4):
                    v = [current[0] + drow[i],current[1] + dcol[i]]
                    if  v[0] >=0 and v[0] < n and v[1] >=0 and v[1] < m:
                        if graph[v[0]][v[1]] == 0:
                            good[tomato].append([v[0],v[1]])
                            graph[v[0]][v[1]] = graph[current[0]][current[1]] + 1                                  
    return graph                                 



          
if dont and good:
    result = bfs(good,graph)
    final = True

    max_list = []
    for i in range(n):
        max_list.append(max(result[i]))
        for j in range(m):
            if result[i][j] == 0:
                final = False
                break         
    if final:
        print(max(max_list)-1)
    else: print(-1) # bfs를 돌렸을 때 안익은게 존재하면 -1
elif not good: print(-1) # 애초애 익은 토마토가 없으면 -1
else: print(0)  #전부 익은 토마토
          
    



    
    
    