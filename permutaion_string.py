"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
   Hide Hint #1  
Obviously, brute force will result in TLE. Think of something else.
   Hide Hint #2  
How will you check whether one string is a permutation of another string?
   Hide Hint #3  
One way is to sort the string and then compare. But, Is there a better way?
   Hide Hint #4  
If one string is a permutation of another string then they must one common metric. What is that?
   Hide Hint #5  
Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?
   Hide Hint #6  
What about hash table? An array of size 26?
"""



from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_len = len(s1)
        s2_len = len(s2)
        
        if s1_len > s2_len:
            return False
        
        s1_count = Counter(s1)
        s2_count = Counter()
        
        if s1_count == s2_count:
            return True
            
        
        for i , char in enumerate(s2):
            s2_count[char] += 1
            if i >= s1_len:
                if s2_count[s2[i - s1_len]] == 1:
                    del s2_count[s2[i - s1_len]]
                else:
                    s2_count[s2[i - s1_len]] -= 1
                
            if s1_count == s2_count:
                return True
        else:
            return False


if __name__ == "__main__":
    sol_obj = Solution()
    print(sol_obj.checkInclusion('ab','eidbaoo'))
