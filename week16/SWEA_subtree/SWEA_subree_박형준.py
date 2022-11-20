# 구글링

def inorder(node, cnt):
    if node == 0:
        return
    cnt[0] = cnt[0] + 1
    inorder(left[node], cnt)
    inorder(right[node], cnt)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    for i in range(0, len(lst), 2):
        par = lst[i]
        chi = lst[i + 1]
        if left[par]:
            right[par] = chi
        else:
            left[par] = chi
    cnt = [0]
    inorder(N, cnt)
    print("#{} {}".format(test_case, cnt[0]))
