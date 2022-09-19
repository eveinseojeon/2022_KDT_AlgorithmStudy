from collections import deque


n,m,k,x = map(int,input().split())
city = {}
for i in range(1,n+1):
    city[i]=[]
for j in range(m):
    n_1,n_2 = map(int,input().split())
    city[n_1].append(n_2)    


def bfs(city,x):
    que = deque([x])
    discovered = [x]
    result = [x]
    while que:
        parent = que.popleft()
        for child in city[parent]:
            if child not in discovered:
                discovered.append(child)
                que.append(child)
                result.append(child + parent)
    
    return discovered,result

discovered, result  = (bfs(city,x))

    
result_2 = []    # 차이를 담는 리스트
for i in range(len(result)):
    result_2.append(result[i] - discovered[i])  
set_result = list(set(result_2))


keys = set_result[k]  #정답 부모값
result_3 = []
