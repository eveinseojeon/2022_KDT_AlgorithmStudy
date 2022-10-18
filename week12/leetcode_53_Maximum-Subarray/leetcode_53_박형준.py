# 구글링(최대부분합)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [-10 ** 4] * len(nums)
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]
        dp[1] = max(nums[1], dp[0] + nums[1])
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)
