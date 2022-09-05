#N,M  = map(int,input())
from collections import deque
from copy import deepcopy

# 가로 : N , 세로 : M
N,M = map(int,input().split())
graph = [list(input()) for _ in range(M)]
W_cnt_list = []
B_cnt_list = []
d_row = (1,-1,0,0)
d_col = (0,0,1,-1)


def W_bfs(s_loc:list,graph:list):
    W_cnt = 1
    W_que = deque([])
    W_que.append(s_loc)
    while W_que:
        c_loc:list = W_que.popleft()
        for i in range(len(d_row)):
            search_loc = [c_loc[0] + d_row[i],c_loc[1] + d_col[i]]
            if (search_loc[0] >= 0 and search_loc[1] >=0 and search_loc[0] <= M-1 and search_loc[1] <= N-1):
                if graph[search_loc[0]][search_loc[1]] == 'W':
                    W_cnt = W_cnt + 1
                    graph[search_loc[0]][search_loc[1]] = 'X'
                    W_que.append(search_loc)
    
    return W_cnt
                


def B_bfs(s_loc:list,graph:list):
    B_cnt = 1
    B_que = deque([])
    B_que.append(s_loc)
    while B_que:
        c_loc:list = B_que.popleft()
        for i in range(len(d_row)):
            search_loc = [c_loc[0] + d_row[i], c_loc[1] + d_col[i]]
            if (search_loc[0] >= 0 and search_loc[1] >=0 and search_loc[0] <= M-1 and search_loc[1] <= N-1):
                if graph[search_loc[0]][search_loc[1]] == 'B':               
                    B_cnt = B_cnt + 1
                    graph[search_loc[0]][search_loc[1]] = 'X'
                    B_que.append(search_loc)
        
    return B_cnt



for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W':
            graph[i][j]='X'
            W_cnt_list.append(W_bfs([i,j],graph))
        elif graph[i][j] == 'B':
            graph[i][j]='X'
            B_cnt_list.append(B_bfs([i,j],graph))
    

print(sum(list(map(lambda x:x**2,W_cnt_list ))),
      sum(list(map(lambda x:x**2,B_cnt_list ))))    
    