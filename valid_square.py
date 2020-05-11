"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # will do with binary operation ti imporve time complexity
        
        if num < 2:
            return True
        
        # will check for the square till num // 2 as for any number min divisor would be 2
        left = 1
        right = num // 2
        
        # as part of binary search / operation will loop till right > = left 
        while left <= right:
            mid = (left + right) // 2
            mid_sqr = mid ** 2
            # here above i have taken square value in a variable to avoid multiple calculation of mid **2 
            # this also imporves the rum time of the program
            
            if mid_sqr == num:
                # number found return True
                return True
            
            elif mid_sqr > num:
                right = mid - 1
                
            else:
                left = mid + 1
                
        
        return False