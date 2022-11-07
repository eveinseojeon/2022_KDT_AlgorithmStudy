class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums) != 1:
            new_nums = [0] * (len(nums) - 1)
            for i in range(len(new_nums)):
                x = nums[i] + nums[i + 1]
                if x == 0:
                    new_nums[i] = 0
                else:
                    new_nums[i] = x % 10
            nums = new_nums
        return nums[0]
