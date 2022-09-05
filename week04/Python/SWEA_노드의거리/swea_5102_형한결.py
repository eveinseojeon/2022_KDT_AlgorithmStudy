from collections import deque

def bfs(start,goal,graph):
    discovered = [start]
    que = deque([start])
    check[start] = 0
    while que:
        parent = que.popleft()
        for child in graph[parent]:
            if child == goal:
                return check[parent] + 1     
            elif child not in discovered:
                discovered.append(child)
                que.append(child)
                check[child] = check[parent] + 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    v,e = map(int,input().split())
    graph = dict()
    check = dict()
    
    for i in range(1,v+1):
        graph[i] = []
        check[i] = 0
    
    for _ in range(e):
        m,n = map(int,input().split())
        graph[m].append(n)
        graph[n].append(m)
    
    
    start,goal =  map(int,input().split())

    print(f"#{test_case} {bfs(start,goal,graph)}")
            
            