from collections import deque


def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    que = deque()
    que.append(root)
    
    while que:
        temp = 0
        for i in range(len(que)):
            cur = que.popleft()
            
            if cur.left:
                que.append(cur.left)
            
            if cur.right:
                que.append(cur.right)
            
            temp += cur.val
    
    return temp
