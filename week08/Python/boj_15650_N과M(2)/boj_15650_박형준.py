import sys
import itertools

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
nCr = itertools.combinations(arr, M)
for c in nCr:
    print(*c)
