"""
https://leetcode-cn.com/problems/move-zeroes/
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i,j=0,0
        l = len(nums)
        while i < l:
            if(nums[i]==0):
                None
            else:
                nums[j] = nums[i]
                j+=1
            i+=1
        while j<l:
            nums[j]=0
            j +=1
        """
        Do not return anything, modify nums in-place instead.
        """
