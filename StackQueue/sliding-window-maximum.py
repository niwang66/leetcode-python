# https://leetcode.cn/problems/sliding-window-maximum/
# timeout
from typing import List
import math

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0,len(nums)-k+1):
            max_value = max(nums[i:i+k])
            res.append(max_value)
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    solution = Solution()
    res = solution.maxSlidingWindow(nums,k)
    print(res)
