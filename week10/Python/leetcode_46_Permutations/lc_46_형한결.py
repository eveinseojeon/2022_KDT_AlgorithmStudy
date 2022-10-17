class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        def dfs(candidate,path=[],results=[]): 
            
            if len(candidate) == 0:
                results.append(path[:])

            for child in candidate:
                next_candidate = candidate[:]
                next_candidate.remove(child)
                path.append(child)
                dfs(next_candidate,path,results)
                path.pop()
            return results

      
        return dfs(nums)