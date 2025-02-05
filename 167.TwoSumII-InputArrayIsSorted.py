"""
167. Two Sum II - Input Array is Sorted

Time Complexity: O(n)

"""

def twoSum(self, numbers, target):
    """
    numbers: List[int]
    target: int
    rtype: List[int]
    """
    l, r = 0, len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum < target:
            l += 1
        elif curSum > target:
            r -= 1
        else:
            return [l+1, r-1]
    
    return []