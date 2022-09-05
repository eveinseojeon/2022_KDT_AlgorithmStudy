iron_bar = list(input())
stack = []
cnt = 0


for i,iron in enumerate(iron_bar):
    
    if iron == '(':
        stack.append(i)
    else:
        if iron_bar[i-1] == '(':
            stack.pop()
            cnt = cnt + len(stack)
            
        else:
            stack.pop() # a막대기가 끝났을떄 ( pop
            cnt = cnt+1

print(cnt)
    