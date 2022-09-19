""" 
1. 정사각형으로 나가면 game over
2. 출발지점 : graph[0][0]
3. 이동 가능 방향 : 오른쪽, 아래
4. 도착지점 : graph[n-1][n-1] = -1
5. 이동할 수 있는 칸의 수  = 밝고 있는 타일숫자
6. 도착 : HaruHaru, 실패 : Hing
"""

from collections import deque
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

def bfs(graph:list)-> str:
    result = "Hing"
    que = deque([[0,0]])
    discovered = [[0,0]]
    while que:
        c_loc = que.popleft()
        tile = graph[c_loc[0]][c_loc[1]]
        d_row = (0,tile)
        d_col = (tile,0)
        for i in range(len(d_row)):
            s_loc = [c_loc[0] + d_row[i],c_loc[1] + d_col[i]]
            if s_loc[0] >= 0 and s_loc[1] >=0 and s_loc[1] < n and s_loc[0] <n:
                if graph[s_loc[0]][s_loc[1]] == -1:
                    result = "HaruHaru"
                    return result
                elif s_loc not in discovered:
                    discovered.append(s_loc)
                    que.append(s_loc)
    return result


print(bfs(graph))



