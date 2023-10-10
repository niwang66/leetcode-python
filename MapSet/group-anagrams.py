
# https://leetcode.cn/problems/group-anagrams/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dic = {}
        for word in strs:
            char_list = list(word)
            char_list.sort()
            word_after_sort = "".join(char_list)
            word_group = word_dic.get(word_after_sort)
            if word_group is None:
                word_dic[word_after_sort] = [word]
            else:
                word_group.append(word)
                word_dic[word_after_sort] = word_group
        res = []
        for _,word_group in word_dic.items():
            res.append(word_group)
        return res

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    res = solution.groupAnagrams(strs)
    print(res)
