"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dict = {}
        for i in magazine:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
                
        for j in ransomNote:
            if j in dict and dict[j] >= 1:
                dict[j] -= 1
                
            else:
                return False
            
        return True
                               
# ====================================================================================
# ====================================================================================
# ====================================================================================


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for item in ransomNote:
            if not item in magazine:
                return False
            magazine = magazine.replace(item, "", 1)
        return True


# ====================================================================================
# ====================================================================================
# ====================================================================================




class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
                return all(ransomNote.count(letter) <= magazine.count(letter) for letter in set(ransomNote))
                
                