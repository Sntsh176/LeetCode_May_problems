"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

"""


class Solution:
    def countBits(self, num: int) -> List[int]:
        # here will use the bit position advantage 
        # it is always true for x//2 == y ( the 1's count will always be <= 1)
        # in case of odd num it will be x//2( 1's ) + 1 and in case of even it will be x//2(1's)
        
        ans = [0]
        # as first pos is already filled for 0, will start from 1
        for i in range(1, num+1):
            if i%2 != 0:
                append_val = ans[i//2]
                ans.append(append_val+1)
            else:
                append_val = ans[i//2]
                ans.append(append_val)
        return ans
        

class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i - (i & -i)] + 1
        return dp