# https://leetcode.cn/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []




if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    res = solution.twoSum(nums,target)
    print(res)
