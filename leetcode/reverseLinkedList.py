# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return

        before = None
        temp = head
        after = temp.next
        while temp != None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before
