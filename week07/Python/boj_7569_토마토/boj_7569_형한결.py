from collections import deque
M,N,H = map(int,input().split())

# 이미 모든 토마토 익어있으면 0, 모두 익지 못하는 상황 -1


graph =[[list(map(int(input().split()))) for _ in range(N)] for _ in range(H)]


dbatch = (0,0,0,0,-1,1)
drow = (-1,1,0,0,0,0)
dcol = (0,0,-1,1,0,0)


def bfs(graph , start:list):
    que  = deque([])
    que.extend(start)
    while que:
        parrent = que.popleft()
        for i in range(len(drow)):
            pb,pr,pc =  parrent[0], parrent[1], parrent[2]
            vb = dbatch[i] + pb
            vr = drow[i] +  pr
            vc = dcol[i] + pc
            if vb >=0 and vb < H and vr >= 0 and vr < N and vc >= 0 and vc < M:
                if graph[vb][vr][vc] == 0:
                    que.append([vb,vr,vc])
                    graph[vb][vr][vc] = graph[pb][pr][pc] + 1
    
    

start = []
for b in range(H):
    for r in range(N):
        for c in range(M):
            if graph[b][r][c] == 0:
                start.append([b,r,c])

done = False
dont = False

if start == False:
    done = True
else:
    bfs(graph,start)
    max_list = []
    for b in range(H):
        for r in range(N):
            if  0 in graph[b][r]:
               dont = True
               break 
            else:
                max_list.append(max(graph[b][r]))
            
    
if done:
    print(0)
elif dont:
    print(-1)
else:
    print(max(max_list))
              
                    
                
                        
        
    
    
   


