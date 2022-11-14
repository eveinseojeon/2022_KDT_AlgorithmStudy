class Solution:
    def sumEvenGrandparent(self, root: TreeNode,p = None,gp = None) -> int:
        if not root:
            return 0
        if gp and gp.val%2 == 0:
            return root.val+self.sumEvenGrandparent(root.left,root,p)+self.sumEvenGrandparent(root.right,root,p)
            
        return self.sumEvenGrandparent(root.left,root,p)+self.sumEvenGrandparent(root.right,root,p)