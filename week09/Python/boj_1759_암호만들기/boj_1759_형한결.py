M,N = map(int,input().split())
strings = input().split()
import copy

def dfs(strings):
    discovered = []
    stack = copy.deepcopy(strings)
    while stack:
        parent = stack.pop()
        parent = sorted(parent)
        if parent not in discovered:
            discovered.append(parent)
            if len(parent) < M:
                for string in strings:
                    if  string not in parent:
                        child = parent + [string]
                        stack.append(child)
    return discovered


discovered = dfs(strings)
discovered.sort()
for i in discovered:
    if len(i) == M:
        print(''.join(i))
