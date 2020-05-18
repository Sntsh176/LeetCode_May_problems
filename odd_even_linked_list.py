"""

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

"""

"""

EXPLANATION:-
Take a list of nodes 
    1 ->  2 -> 3 -> 4 -> 5 -> null
	  
    We need to modify this list.
	as all odd nodes followed by all even nodes.
	  
	We can get required list, 
	if we can seperate nodes at odd places as one list
	and nodes at even places as one list.
	And at the end, if we merge those two list,
	we will get the required list.
	
	odd list  (which contain all nodes in odd places) -   1 -> 3 -> 5 
	even list  (which contain all nodes in even places) -   2 -> 4 -> null
	
    We can do this by taking two pointers
	  1. odd pointer  -> which iterates over nodes in odd places
	  2. even pointer  -> which iterates over nodes in even places
      
      
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # here the task is basically on basis of index arrange the odd( first ) and even w.r.t 
        # to relative order 
        
        # as 1st item is odd index / node number and 2nd will be even
        # will push the even index at the end and will do the next variable modification iteratively till end
        if not head or head.next == None:
            return head
            
        odd = head
        even = head.next
        even_head = head.next
        
        # now will loop to the nodes and depending on the even odd will add to the respective Nodes
        while even != None and even.next != None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
            
        # now will add
        odd.next = even_head
        return head