from collections import deque


T = int(input())
for test_case in range(1, T + 1):
    N,M  = map(int,input().split())
    nums = deque(map(int,input().split()))
    for _ in range(M):
        num = nums.popleft()
        nums.append(num)
    print(f'#{test_case} {nums.popleft()}')

