# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))
        
        dummy = ListNode(0)
        result = dummy 

        while minHeap:
            value, index, node = heapq.heappop(minHeap)
            result.next = node 
            result = result.next 
        
            if node.next:
                heapq.heappush(minHeap, (node.next.val, index, node.next))
        
        return dummy.next
# tc O(N logk) where k is size of heap and is total nodes in the problem 
# sc O(k)
