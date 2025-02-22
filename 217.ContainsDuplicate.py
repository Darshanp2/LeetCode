"""
217. Contains Duplicate

Time Complexity: O(n)

"""

def containsDuplicate(self, nums: List[int])->bool:
    dct = {}
    for i in nums:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1
    
    for i in dct.values():
        if i > 1:
            return True
            break
    
    return False