N,M = map(int,input().split())

def dfs():
    board = [x for x in range(1,N+1)]
    stack = [[x] for x in range(1,N+1)]
    discovered = []
    while stack:
        parent = stack.pop()
        parent.sort()
        if (len(parent) <= M) and (parent not in discovered):
            discovered.append(parent)
            for num in board:
                if num not in parent:
                    child = parent + [num]
                    stack.append(child)
    return discovered



discovered = dfs()
discovered.sort()

for i in discovered:
    if len(i)==M:
        print(*i)