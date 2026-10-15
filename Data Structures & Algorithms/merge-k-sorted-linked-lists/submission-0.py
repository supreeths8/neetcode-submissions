# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        class Wrapper:
            def __init__(self, node):
                self.node = node

            def __lt__(self, other):
                return self.node.val < other.node.val

        for l in lists:
            if l:
                heapq.heappush(min_heap, Wrapper(l))

        dummy = ListNode()
        curr = dummy

        while min_heap:
            n = heapq.heappop(min_heap)
            curr.next = n.node
            curr = curr.next

            if curr.next:
                heapq.heappush(min_heap, Wrapper(curr.next))

        return dummy.next
