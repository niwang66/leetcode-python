"""
https://leetcode.cn/problems/reverse-nodes-in-k-group/
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len = 0
        curr = head
        while (curr is not None):
            curr = curr.next
            len += 1
        if(len<2) or (k <2):
            return head
        group_count, loss = divmod(len,k)
        curr = head
        first_group = True
        pre_group_begin = None
        for _ in range (group_count):
            pre = None
            group_begin = curr
            for _ in range (k):
                next = curr.next
                curr.next = pre
                pre = curr
                curr = next
            group_end = pre
            if(first_group):
                head = group_end
                first_group = False
            else:
                pre_group_begin.next = group_end
            pre_group_begin = group_begin
        pre_group_begin.next = curr
        return head
    
def print_list(head: Optional[ListNode]):
    curr = head
    while curr is not None:
        print (curr.val)
        curr = curr.next

if __name__ == '__main__':
    s = Solution()
    l = [1,2,3,4,5]
    len = len (l)
    head = None
    curr, next = None, None
    for i in range(len):
        if(i==0):
            curr = ListNode(val=l[i])
            head = curr
        if i< (len -1):
            next = ListNode(val=l[i+1])
        else:
            next = None
        curr.next = next
        curr = next

    s = Solution()
    head = s.reverseKGroup(head,3)

    print_list(head)
