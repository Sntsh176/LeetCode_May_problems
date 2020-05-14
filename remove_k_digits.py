"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Here the concept is to remove max digit from right
        from right we are checking if it is greater than the previous (left)
        """
        stack = []
        k_value = k
        
        for item in num:
            while k_value and stack and stack[-1] > item:
                stack.pop()
                k_value -= 1
            stack.append(item)
            
        ans = "".join(stack[0:len(num) - k]).lstrip("0")
        
        if len(ans):
            return ans
        else:
            return "0"
            

# ================================================================
# ================================================================
# ================================================================

            
            
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for n in num:
            while k and stack and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
        
        stack = stack[:-k] if k else stack
        #print(stack)
        return "".join(stack).lstrip('0') or "0"