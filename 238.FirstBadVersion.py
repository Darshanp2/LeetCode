"""
238. First Bad Version

- Using Binary Search 

Time Complexity : o(logn)
"""

def firstBadVersion(self, n):

    l = 1
    r = n 

    while l < r:
        m = (l+r)//2
        
        if isBadVersion(m):
            r = m
        else:
            l = m + 1
        
    return l
