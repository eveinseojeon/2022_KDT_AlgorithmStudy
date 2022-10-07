class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        result = []

        def make_comb(num_arr, idx):
            if len(num_arr) == k:
                result.append(num_arr)
                return
            for n in nums[idx:]:
                tmp = num_arr[:]
                tmp.append(n)
                make_comb(tmp, nums.index(n) + 1)
        make_comb([], 0)
        return result
