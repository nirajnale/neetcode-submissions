# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        
        while True:
            # check if there are k nodes left
            kth = prev_group_tail
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            # reverse k nodes
            group_head = prev_group_tail.next
            prev, curr = None, group_head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # connect reversed group
            prev_group_tail.next = prev
            group_head.next = curr
            prev_group_tail = group_head