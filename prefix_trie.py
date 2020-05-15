"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['#'] = '#'
        """
        The above will create some data structure
        word = 'note' and 'nord'
        {'n': {'o': {'t': {'e': {'#': '#'}}, 'r': {'d': {'#': '#'}}}}}
        and '#' represent the end of the word , and after that a new word is getting started
        """
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        word = 'note' and 'nord'
        {'n': {'o': {'t': {'e': {'#': '#'}}, 'r': {'d': {'#': '#'}}}}}
        serach for the letter/char and then go for the sub - dictionary
        """
        t = self.trie
        for char in word:
            if char not in t:
                return False
            t = t[char]
        if '#' in t:
            return True
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for char in prefix:
            if char not in t:
                return False
            t = t[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)