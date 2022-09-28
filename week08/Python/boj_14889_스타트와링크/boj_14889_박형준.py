import sys
import itertools


def team_abil(board, arr):
    res = 0
    arr_nPr = list(itertools.permutations(arr, 2))
    for i, j in arr_nPr:
        res += board[i][j]
    return res


input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
nCr = list(itertools.combinations(range(N), N // 2))
res_list = []
for i in range(len(nCr)):
    team_a = team_abil(board, nCr[i])
    team_b_arr = [j for j in range(N) if j not in nCr[i]]
    team_b = team_abil(board, team_b_arr)
    res_list.append(abs(team_a - team_b))
print(min(res_list))
