# 구글링

def insert_heap(heap, data):
    heap.append(data)
    index = len(heap) - 1
    while index > 1 and heap[index] < heap[index // 2]:
        heap[index], heap[index // 2] = heap[index // 2], heap[index]
        index //= 2


def get_node_idx(N):
    par = []
    while (N != 0):
        N = N // 2
        par.append(N)
    return par


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    n_list = list(map(int, input().split()))
    answer = []
    par = get_node_idx(N)
    heap = [0]
    for i in n_list:
        insert_heap(heap, i)
    for i in par:
        answer.append(heap[i])
    print(f'#{test_case} {sum(answer)}')
