"""
424. Longest Repeating Character Replacement
Time Complexity:  O(n)
"""

def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    result = 0 
    maxFreq = 0
    count = {}

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxFreq = max(maxFreq, count[s[r]])

        while (r - l + 1) - maxFreq > k:
            count[s[l]] -= 1
            l += 1
        
        result = max(result, r - l + 1)
    
    return result