# 1. push하는 순서는 반드시 오름차순


'''
ans = []
N = int(input())
for _ in range(N):
    num = int(input())
    ans.append(num)
'''
from collections import deque
N = 8
ans = deque([4,3,6,8,7,5,2,1])
stack = []
current = []
#sorted_ans = [1,2,3,4,5,6,7,8]



# append 하다가 정답 만났을때 pop
# 8(max)뒤의 숫자가 내림차순이 아니면 'NO'

for i in ans:
    for j in sorted(ans):
        if ans[i] == max(ans):
            if ans[i:] != sorted(ans[i:],reveres=True):       
                print('no')        
        if j not in current:
            current.append(j)
            stack.append(j)
            print('+')
        if ans[i] in stack:
            stack.pop()
            print('-')
        continue    
            
            