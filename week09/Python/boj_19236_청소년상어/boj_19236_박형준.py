import sys

input = sys.stdin.readline
fish_num = []
fish_dir = []
for _ in range(4):
    tmp = list(map(int, input().strip().split()))
    for i in range(0, 8, 2):
        fish_num.append(tmp[i])
        fish_dir.append(tmp[i + 1])

