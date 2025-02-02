"""
49. Group Anagrams

Time Complexity: O(m*n)
"""

from collections import defaultdict

def groupAnagrams(self, strs):

    anagrams = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        anagrams[tuple(count)].append(word)
    
    return list(anagrams.values())
