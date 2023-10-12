
# https://leetcode.cn/problems/generate-parentheses/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.recur(0,0,n,"")
        return  self.res
    def recur(self, left, right, n, s):
        if left == n & right ==n:
            self.res.append(s)
            return
        if left < n:
            self.recur(left+1, right, n, s+"(")
        if right < left:
            self.recur(left, right + 1, n, s + ")")


if __name__ == '__main__':
    solution = Solution()
    res = solution.generateParenthesis(4)
    print(res)

