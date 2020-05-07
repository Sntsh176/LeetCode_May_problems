"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

from collections import Counter

# will use Counter module in our algorithm which makes problem a lot simpler 
# this will retunr key , value ( as count of that char in the string )

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        counter = Counter(s)
        # This will return belo for string s = "leetcode"
        # Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
        
        for item, freq in counter.items():
            if freq == 1:
                # if count is 1 then retunr it's position using find function of string
                return s.find(item)
        # if loop exhausted then else will return -1 as needed          
        else:
            return -1
        