"""
128. Longest Consecutive Sequences

Time Complexity: O(n)

"""

def longestConsecutive(self, nums):

    longest = 0
    nums_set = set(nums)
    for n in nums_set:
        if (n-1) not in nums_set:
            length = 1
            while (n + length) in nums_set:
                length += 1
            longest = max(longest, length)
        
    return longest