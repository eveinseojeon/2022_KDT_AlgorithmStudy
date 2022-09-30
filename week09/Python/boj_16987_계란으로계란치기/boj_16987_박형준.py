# 구글링

import sys

input = sys.stdin.readline
N = int(input())
dur_eggs = [0] * N
wei_eggs = [0] * N
for i in range(N):
    dur_eggs[i], wei_eggs[i] = map(int, input().split())

result = 0


def break_egg(idx, dur_eggs):
    global result
    if idx == N:
        cnt = 0
        for x in dur_eggs:
            if x <= 0:
                cnt += 1
        if cnt > result:
            result = cnt
        return
    if dur_eggs[idx] > 0:
        for j in range(N):
            flag = False
            if (dur_eggs[j] > 0) and (j != idx):
                flag = True
                tmp = dur_eggs[:]
                tmp[idx] -= wei_eggs[j]
                tmp[j] -= wei_eggs[idx]
                break_egg(idx + 1, tmp)
        if not flag:
            break_egg(idx + 1, dur_eggs)
    else:
        break_egg(idx + 1, dur_eggs)


break_egg(0, dur_eggs)
print(result)
