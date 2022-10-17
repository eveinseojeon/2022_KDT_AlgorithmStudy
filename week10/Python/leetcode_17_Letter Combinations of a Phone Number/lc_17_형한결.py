class Solution:
    def __init__(self):
        self.phone ={"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
    def letterCombinations(self, digits: str) -> list[str]:  #digits  : "23"
                
        def dfs(index, path,result = []): #1 : dfs(0,"")  #2 : dfs(1,"a")
          
            if len(path) == len(digits):
                result.append(path)
                return 
            
            for i in range(index, len(digits)): #1 : (0,2)  #2 : (1,2)
                for j in self.phone[digits[i]]: #1 : j  in self.phone["2"] #2 : j in self.phone["3"]
                    dfs(i+1,path+j,result)
                    
            return result    
                
    
    
        if not digits:
            result = []
            return result
        
        else:
            return dfs(0,"")

                        