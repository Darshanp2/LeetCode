"""
347. Top K frequent element

Time Complexity : O(n*logn)

Using Hashmap and Tuple
"""

def topKFrequent(self, nums, k):

    dict1 = {}
    for i in nums:
        if i in dict1:
            dict1[i] += 1
        else:
            dict[i] = 1
    
    sortedValues = sorted(dict.items(), key = lambda x : x[1], reverse = True)

    return [item[0] for item in sortedValues[:k]]

"""
Different Approach - Using Hashmap and MinHeap

Time Complexity: O(n*logk)

"""
import heapq
def topKFrequent(self, nums, k):

    dict1 = {}
    heap = []
    for i in dict1:
        if i not in dict:
            dict1[i] = 1
        else:
            dict1[i] += 1
        
    for key, val in dict1.items():
        if len(heap) < k:
            heapq.heappush(heap, (val, key))
        else:
            heapq.heappushpop(heap, (val, key))
        

    return [h[1] for h in heap]