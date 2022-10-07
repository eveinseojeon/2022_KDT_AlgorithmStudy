class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def make_perm(num_arr):
            if len(num_arr) == len(nums):
                result.append(num_arr)
                return
            for i in nums:
                if i not in num_arr:
                    tmp = num_arr[:]
                    tmp.append(i)
                    make_perm(tmp)
        make_perm([])
        return(result)