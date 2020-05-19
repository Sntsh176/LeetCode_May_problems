"""
Find All Anagrams in a String
Solution
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


from collections import Counter

class Solution:
    
    # Solution 1 : Sliding Window, Hash Table
    def findAnagrams(self, s, p):
        cnt_p = Counter(p); n = len(s); m = len(p); res = []
        for i in range(n-m+1):
            if i == 0: cnt_s = Counter(s[:m])
            else:
                prev = s[i-1]; curr = s[i+m-1]
                cnt_s[prev] -= 1; cnt_s[curr] += 1
                if cnt_s[prev] == 0: del cnt_s[prev]
            if cnt_s == cnt_p: res.append(i)
        return res        
        
		
    # Solution 2 : Hash Table
    def findAnagrams2(self, s, p):
        cnt_p = Counter(p); n = len(s); m = len(p); res = []
        for i in range(n-m+1):
            cnt_s = Counter(s[i:i+m])
            if cnt_s == cnt_p: res.append(i)
        return res     
        
# ===============================================================
# ===============================================================
# ===============================================================
        
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)==0:return []
        pri=[2, 3, 5, 11, 19, 23, 37, 47, 59, 79, 97, 113, 137, 163, 191, 223, 257, 293, 331, 353, 383, 431, 487, 541, 587, 631]
        dct={}
        res=[]
        for c in "qwertyuiopasdfghjklzxcvbnm":
            dct[c]=pri[ord(c)-ord("a")]
        target=0
        for i in p:
            target+=dct[i]
        ln=len(p)
        
        sm=0
        l=0
        for i in range(len(s)):
            sm+=dct[s[i]]
            l+=1
            if l==ln:
                if sm==target:res.append(i-ln+1)
                sm-=dct[s[i-ln+1]]
                l-=1
            
            
        return res
        
# ===============================================================
# ===============================================================
# ===============================================================        

from collections import Counter

class Solution:
    def findAnagrams(self,s,p):
        
        s_len = len(s)
        p_len = len(p)
        
        if s_len < p_len:
            return []
        
        result = []
        p_count = Counter(p)
        s_count = Counter()
        
        for i in range(s_len):
            s_count[s[i]] += 1
            if i >= p_len:
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]
                else:
                    s_count[s[i - p_len]] -= 1
                    
            if p_count == s_count:
                result.append(i - p_len + 1)
                
        return result


if __name__ == "__main__":
    sol_obj = Solution()
    print(sol_obj.findAnagrams('abab','ab'))