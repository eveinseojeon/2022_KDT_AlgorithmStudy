N,M = map(int,input().split())
 

def dfs():
    board = [x for x in range(1,N+1)]
    stack = [[x] for x in range(1,N+1)]
    result = []
    while stack:
        parent = stack.pop()
        if len(parent) == M:
            result.append(parent)
        elif len(parent) < M:
            for num in board:
                if num not in parent:
                    child = parent + [num]
                    stack.append(child)
    return result



result = dfs()
result.sort()
for i in result:
    print(*i)