"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        # here will have a dict for storing given values position and parent
        # for true parent have to be diff and values should be equal to ( x, y)
        
        search_values = []
        
        # using recursive function
        def search_dfs(node , depth , parent):
            
            if node is None:
                return
            
            # wil check for the x,y values
            if node.val == x or node.val == y:
                # make an entry into the  search_values list
                search_values.append((depth,parent))
            
            search_dfs(node.left , depth + 1 , node)
            search_dfs(node.right , depth + 1 , node)
            
        
        search_dfs(root , 0 , None)
        
        return search_values[0][0] == search_values[1][0] and search_values[0][1] != search_values[1][1]
        
        