# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # [1,2,3,4,5]                      temp   prev current
        # [5,4,3,2,1]   [5->4->3->2->1]    #None  #5     #None

        # current is head
        # set previous to None
        # repeat this till current becomes None
                # store next of current element to temp to use it later.
                # make next of current element previous
                # save this node to previous variable
                # move to next element using temp 
        
        # return previous 
        
        current = head
        previous = None 

        while current:
            temp = current.next
            current.next = previous
            previous = current 
            current = temp 

        return previous

        # tc O(n)
        # sc O(1)