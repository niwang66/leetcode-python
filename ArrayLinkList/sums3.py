from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        nums.sort()
        print(nums)
        previousK = ""
        for i in range (n-2):
            k = nums[i]
            if(k == previousK):
                continue
            left = i+1
            right = n-1
            previousLeft = ""
            while (right>left):
                if(previousLeft == nums [left]):
                    left += 1
                    continue
                sum = nums[i] + nums [left] + nums[right]
                if(sum == 0):
                    res.append([nums[i], nums[left], nums[right]])
                    previousK = k
                    previousLeft = nums[left]
                    left += 1
                    right -= 1
                elif(sum>0):
                    right -=1
                else:
                    left +=1
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
    print(s.threeSum(nums))