from typing import List
class Solution:
    def  moveZeroes(self, nums: List[int]) -> None:
        print("Function called")
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] , nums[j] = nums[j] , nums[i]
                i+=1

n = Solution()
nums = [0,1,0,3,12]
n.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]