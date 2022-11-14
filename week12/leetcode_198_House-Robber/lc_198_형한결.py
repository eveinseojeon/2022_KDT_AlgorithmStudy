class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if len(nums)<=2:
            return max(nums)
        
        elif len(nums) ==3:
            return max(nums[1],nums[0] + nums[2])
        
        else:
            dp = [0 for x in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = nums[0] + nums[2]
            for i in range(3,len(nums)):
                if dp[i-2]> dp[i-3]:
                    dp[i] = dp[i-2] + nums[i]
                    
                else:
                    dp[i] = dp[i-3] + nums[i]
            
            return max(dp)
        
        
my_solution - 
                    

                
        