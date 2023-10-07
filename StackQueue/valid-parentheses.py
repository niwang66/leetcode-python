"""
https://leetcode.cn/problems/valid-parentheses/description/
"""
from typing import Optional


class Solution:
    def isValid(self, s: str) -> bool:
        l = list()
        for c in s:
            if c == "(" or c == "[" or c == "{":
                l.append(c)
            elif c == ")" and len(l) > 0:
                if l[-1] == "(":
                    l.pop()
                else:
                    return False
            elif c == "]" and len(l)> 0:
                if l[-1] == "[":
                    l.pop()
                else:
                    return False
            elif c == "}" and len(l) > 0:
                if l[-1] == "{":
                    l.pop()
                else:
                    return False
            else:
                return False
        return len(l) == 0


if __name__ == '__main__':
    str1 = "()[]{}"
    s = Solution()
    print(s.isValid(str1))
