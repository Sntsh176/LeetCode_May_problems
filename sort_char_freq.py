"""
Sort Characters By Frequency
Solution
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        
        dict = collections.Counter(s)
        return ''.join(c*x for x,c in dict.most_common())
        
    
# =====================================================================    
# =====================================================================
# =====================================================================        
        
        
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()
        for c in s:
            if c in freq:
                freq[c]+=1
            else:
                freq[c]=1
        freq_r = dict()
        for k,v in freq.items():
            if v in freq_r:
                freq_r[v].append(k)
            else:
                freq_r[v]=[k]
        
        freq_list = list(freq_r.keys())
        freq_list.sort(reverse=True)
        output = ""
        for f in freq_list:
            for c in freq_r[f]:
                for i in range(f):
                    output+=c
        return output