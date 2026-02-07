#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root ==p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
            
        return left if left else right


            # #base case
            # if root[index] is None:
            #     return 

            # dfs(2*index + 1, end ) #왼쪽 자식이 있는지 검사
            # dfs(2*index + 2, end ) #오른쪽 자식이 있는지 검사
            
            # return 



        p_index = dfs(0, p)
        q_index = dfs(0, q)

        LCA(p_index, q_index)
