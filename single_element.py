
"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space.
"""




class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1

        while l < r:
            mid = l + (r - l) // 2
            even_halves = (mid % 2 == 0)

            if nums[mid] == nums[mid+1]:
                if even_halves:
                    l = mid+2
                else:
                    r = mid-1
            elif nums[mid-1] == nums[mid]:
                if even_halves:
                    r = mid-2
                else:
                    l = mid+1
            else:
                return nums[mid]
            
        return nums[l]


# ===============================================================
# ===============================================================
# ===============================================================


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while True:
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1
            if mid < high and nums[mid] == nums[mid+1]:
                low = mid + 2
            elif mid > low and nums[mid] == nums[mid-1]:
                high = mid - 2
            else:
                return nums[mid]

# ===============================================================
# ===============================================================
# ===============================================================
    
                
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sum(set(nums))*2 - sum(nums)