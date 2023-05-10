"""
https://leetcode.cn/problems/swap-nodes-in-pairs
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return None


def print_list(head: Optional[ListNode]):
    curr = head
    while curr is not None:
        print (curr.val)
        curr = curr.next

if __name__ == '__main__':
    s = Solution()
    l = [1,2,3,4]
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
    head = s.swapPairs(head)
    print_list(head)

