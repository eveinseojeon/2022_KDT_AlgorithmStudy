import sys

# combination 구현은 구글링 참조


def comb(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in comb(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result


def vowel_filter(lst, nums):
    vowel_lst = ['a', 'e', 'i', 'o', 'u']
    for i in nums:
        if lst[i] in vowel_lst:
            return 1
    return 0


def consonant_filter(lst, nums):
    vowel_lst = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for i in nums:
        if lst[i] not in vowel_lst:
            cnt += 1
    if cnt < 2:
        return 0
    return 1


input = sys.stdin.readline
L, C = map(int, input().split())
chars = list(input().split())
chars.sort()
nums = [i for i in range(C)]
nums_list = comb(nums, L)
for i in nums_list:
    if vowel_filter(chars, i) == 0:
        continue
    if consonant_filter(chars, i) == 0:
        continue
    for j in i:
        print(chars[j], end='')
    print(end='\n')
