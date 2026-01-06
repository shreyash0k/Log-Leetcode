class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None 
        current = head 

        while current is not None:
            temp = current.next 

            current.next = previous 

            previous = current 

            current = temp 

        return previous 
        
# time complexity - O(n)
# space complexity - O(1)