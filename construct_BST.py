"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
        Function to get TreeNode for given preorder list / linked list
        Param:
        preorder : list of item which will be in tree
        Return :
        return type will be TreeNode as given in above class
        """
        
        # length of the tree
        n = len(preorder)
        return self.tree_construct(preorder, 0, n)
        
    def tree_construct(self, preorder , left , right):
        # this function will be called recursively 
        # will check each time if the root is > right then it means we have come to leaf node so return NULL
        if left >= right:
            return None
            
        # Now will create root object for each root/subroot with root value of the argument
        root = TreeNode(preorder[left])
        # increment the value to move to next item 
        i = left + 1
        
        while (i < right and preorder[i] < root.val):
            i += 1
            
        root.left = self.tree_construct(preorder , left+1 , i)
        root.right = self.tree_construct(preorder, i, i+(right-i))
        
        
        return root
        
        
# ========================================================================        
# ========================================================================
# ========================================================================
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        head = TreeNode(preorder[0])
        for node in preorder[1:]:
            newnode = TreeNode(node)
            searchnode = head
            while 1:
                if searchnode.val > newnode.val:
                    if searchnode.left == None: 
                        searchnode.left = newnode
                        break
                    searchnode = searchnode.left
                else:
                    if searchnode.right == None: 
                        searchnode.right = newnode
                        break
                    searchnode = searchnode.right
        return head
    
    