import sys
import itertools

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
nPr = itertools.permutations(arr, M)
for p in nPr:
    print(*p)