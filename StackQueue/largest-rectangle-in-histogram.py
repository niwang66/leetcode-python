
# https://leetcode.cn/problems/largest-rectangle-in-histogram/
# timeout
from typing import List
import math

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = -math.inf-1
        length = len(heights)
        if length == 1:
            return heights[0]
        if length == 0:
            return 0
        for i in range(0,length):
            right = left = i
            left_small = right_samll = True
            for left in range(i,-1,-1):
                if heights[left]<heights[i]:
                    left_small = False
                    break
            for right in range(i+1,length):
                if heights[right] < heights[i]:
                    right_samll = False
                    break
            if right_samll:
                right +=1
            if left_small:
                left -=1
            one_res = heights[i] * (right-left-1)
            # print(left, right)
            # print(one_res)
            if one_res>res:
                res = one_res
        return res



if __name__ == '__main__':
    heights = [2,3]
    solution = Solution()
    res = solution.largestRectangleArea(heights)
    print(res)
