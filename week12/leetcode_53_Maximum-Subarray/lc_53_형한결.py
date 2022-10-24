class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        
        sum_list = []
        skip_index = 0

        for i in range(len(nums)): 
            if nums[i]>0 and i >= skip_index:
                dp = [0 for x in range(len(nums))]
                dp[0]=nums[i]
                index = i
                for j in range(1,len(nums)-i):
                    index = index + 1
                    if dp[j-1]+nums[index] > 0:
                        dp[j] = dp[j-1]+nums[index]
                    else:
                        sum_list.append(max(dp))
                        skip_index = index
                        break
                sum_list.append(max(dp)) 
        if sum_list:
            return max(sum_list)
        
        else: 
            return max(nums)
            
            
 
 
my_solution = Solution()
print(my_solution.maxSubArray([5,4,-1,7,8]))




