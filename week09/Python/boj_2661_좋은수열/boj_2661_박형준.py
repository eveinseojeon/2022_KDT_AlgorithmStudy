import sys


def good_seq(lst, lst_len):
    lst.reverse()
    for k in range(1, (lst_len // 2) + 1):
        if lst[:k] == lst[k:2 * k]:
            lst.reverse()
            return 0
    lst.reverse()
    return 1


def make_seq(new_seq, N):
    if len(new_seq) == N:
        return
    nums = [1, 2, 3]
    for num in nums:
        new_seq.append(num)
        if good_seq(new_seq, len(new_seq)) == 1:
            make_seq(new_seq, N)
            if len(new_seq) == N:
                return
            else:
                del new_seq[-1]
        else:
            del new_seq[-1]


input = sys.stdin.readline
N = int(input())
new_seq = []
make_seq(new_seq, N)
print(*new_seq, sep='')
