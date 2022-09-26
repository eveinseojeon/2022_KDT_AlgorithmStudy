import sys
import itertools


def make_ops_arr(ops):
    ops_arr = []
    for i in range(ops[0]):
        ops_arr.append('+')
    for i in range(ops[1]):
        ops_arr.append('-')
    for i in range(ops[2]):
        ops_arr.append('*')
    for i in range(ops[3]):
        ops_arr.append('//')
    return ops_arr


def calculator(cal_list, N):
    res = cal_list[0]
    for i in range(1, (2 * N) - 1, 2):
        if cal_list[i] == '+':
            res = res + cal_list[i + 1]
        elif cal_list[i] == '-':
            res = res - cal_list[i + 1]
        elif cal_list[i] == '*':
            res = res * cal_list[i + 1]
        elif cal_list[i] == '//':
            if (res < 0) and (cal_list[i + 1] > 0):
                res = -(-res // cal_list[i + 1])
            else:
                res = res // cal_list[i + 1]
    return res


input = sys.stdin.readline
N = int(input())
num_arr = list(map(int, input().split()))
ops = list(map(int, input().split()))
ops_arr = make_ops_arr(ops)
nPr = list(itertools.permutations(ops_arr, N - 1))
nPr = list(set(nPr))
case = len(nPr)
res_list = []
for i in range(case):
    cal_list = []
    for j in range(N):
        cal_list.append(num_arr[j])
        if j != N - 1:
            cal_list.append(nPr[i][j])
    res_list.append(calculator(cal_list, N))
res_list.sort()
print(res_list[-1])
print(res_list[0])
