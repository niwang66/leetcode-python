from builtins import str

# https://leetcode.cn/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dic = {")":"(","}":"{","]":"["}
        left_parentheses_list = ("(","{","[")
        l = list()
        for c in s:
            if c in left_parentheses_list:
               l.append(c)
            else:
                left_parentheses = parentheses_dic[c]
                if len(l)>0 and l[-1] == left_parentheses:
                    l.pop()
                else:
                    return False
        return len(l) == 0


if __name__ == '__main__':
    s = "]"
    solution = Solution()
    res = solution.isValid(s)
    print(res)
