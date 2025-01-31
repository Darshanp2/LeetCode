"""
53. Maximum Subarray

Using Dynamic Programming 

Time Complexity: O(n)
"""
def maxSubarray(self, nums):
    maxSum = nums[0]
    curSum = 0 

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSum = max(maxSum, curSum)
    
    return maxSum