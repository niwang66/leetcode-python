'''
https://leetcode.cn/problems/linked-list-cycle-ii/
'''
f'''
https://leetcode.cn/problems/linked-list-cycle/
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        curr = head
        while curr is not None:
            if curr in s:
                return curr
            else:
                s.add(curr)
                curr = curr.next
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
    print(s.detectCycle(head))
