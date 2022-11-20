# 구글링

def make_tree(node, tree, number, N):
    if node <= N:
        make_tree(node * 2, tree, number, N)
        tree[node] = number[0]
        number[0] += 1
        make_tree((node * 2) + 1, tree, number, N)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    number = [1]
    make_tree(1, tree, number, N)
    print(f"#{test_case} {tree[1]} {tree[N // 2]}")