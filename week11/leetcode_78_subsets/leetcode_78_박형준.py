class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def make_subset(arr, idx, nums):
            result.append(arr)
            for i in nums[idx:]:
                if i not in arr:
                    tmp = arr[:]
                    tmp.append(i)
                    make_subset(tmp, nums.index(i) + 1, nums)
        make_subset([], 0, nums)
        return result
