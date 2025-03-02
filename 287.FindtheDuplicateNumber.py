"""
287. Find the Duplicate Number

Time Complexity: O(N)
Space Complexity: O(1)

"""

def findDuplicate(self, nums: List[int]) -> int:
    slow, fast = 0, 0

    while True:
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]
        if slow == fast:
            break

    slow2 = 0 
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow 
        
