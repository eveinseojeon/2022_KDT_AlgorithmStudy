class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0] * (len(nums) + 2)
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for n in range(2, len(nums)):
            dp[n] = max(dp[n - 2] + nums[n], dp[n - 1])
        return max(dp)
