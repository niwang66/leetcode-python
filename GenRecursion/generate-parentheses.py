#https://leetcode.cn/problems/generate-parentheses/
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.rec(0,2*n,"")
        return None
    def rec(self,level,n,s):
        if level == n:
            print(s)
            return
        self.rec(level + 1, n, s + "(")
        self.rec(level + 1, n, s + ")")

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))