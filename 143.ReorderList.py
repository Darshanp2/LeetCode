"""
143. Reorder List 

Time Complexity: O(N)
Space Complexity: O(1)

"""
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next 

def reorderList(self, head: Optional[ListNode])->None:

    #Using two pointers finding the middle of the linked list 
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #Reversing the second part of the list 
    second = slow.next
    prev = None
    slow.next = None

    while second:
        tmp = second.next
        second.next = prev
        prev = second 
        second = tmp 

    #Merging both the list 
    first = head 
    second = prev 
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first = temp1 
        second = temp2 


