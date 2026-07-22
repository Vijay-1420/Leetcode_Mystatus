# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return none
        point_1=headA
        point_2=headB
        while point_1 != point_2:
            point_1 = point_1.next if point_1 else headB
            point_2 = point_2.next if point_2 else headA
        return point_1