"""Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # will use Counter to check the repeated items with count
        # using most_common() method which will give most common to less common sorted items
        
        count_list = Counter(nums).most_common()
        
        # return the 1st item which will be most common
        return count_list[0][0]
        
        
        
        
# ===========================================================
# ===========================================================
# ===========================================================



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority element is the element that appears more
        #than n/2 times
        
        nums.sort()
        
        # at n/2 pos majority element will always be threre as it is already confirmed
        majority_ele = nums[int(len(nums)//2)]
        return majority_ele