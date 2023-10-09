#https://leetcode.cn/problems/valid-anagram/description/
class Solution:
    def isAnagramSort(self, s: str, t: str) -> bool:
        s_char = list(s)
        s_char.sort()
        t_char = list(t)
        t_char.sort()
        return s_char == t_char

    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for c in s:
            count = dic.get(c)
            if count is None:
                dic[c] = 1
            else:
                dic[c] = dic[c] + 1
        for c in t:
            count = dic.get(c)
            if count is None:
                return False
            else:
                dic[c] = dic[c] - 1
        for k,v in dic.items():
            if v != 0:
                return False
        return True



if __name__ == '__main__':
    s = "rat"
    t = "car"
    solution = Solution()
    res = solution.isAnagram(s,t)
    print(res)