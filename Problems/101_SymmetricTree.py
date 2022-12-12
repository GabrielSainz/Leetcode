'''
100. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


Example: 
Input: root = [1,2,2,3,4,4,3]
Output: true
'''

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def isSameTree(self, p, q) -> bool:
        if not p and not q: 
            return True
        if not p or not q or p.val != q.val: 
            return False
        
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
        
       
    def isSymmetric(self, root) -> bool:

        return self.isSameTree(self.left, self.left)


p = 1
if not p: 
    print(True)