"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
   Hide Hint #1  
Try to utilize the property of a BST.
   Hide Hint #2  
Try in-order traversal. (Credits to @chan13)
   Hide Hint #3  
What if you could modify the BST node's structure?
   Hide Hint #4  
The optimal runtime complexity is O(height of BST).

"""


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.count = 0
        self.result = 0
        
        def kth_small(root):
            if root.left: kth_small(root.left)
            
            self.count += 1
            if self.count == k:
                self.result = root.val
                return
            
            if root.right: kth_small(root.right)
            
        kth_small(root)
        return self.result
    
# ===============================================================
# ===============================================================
# ===============================================================


from itertools import islice, chain
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def lazyinorder(root):
            if root:
                yield from chain(lazyinorder(root.left), (x for x in [root.val]), lazyinorder(root.right))
        return next(islice(lazyinorder(root), k-1, k))
    
    
    
        