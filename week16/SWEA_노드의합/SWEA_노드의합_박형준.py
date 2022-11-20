# 구글링

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for i in range(M):
        par, chi = map(int, input().split())
        tree[par] = chi
    for i in range(N, 0, -1):
        tree[i // 2] += tree[i]
    print(f'#{test_case} {tree[L]}')
