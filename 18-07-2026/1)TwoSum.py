from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in nummap:
                return [nummap[complement], i]
            nummap[num] = i

nums = [2, 7, 11, 15, 18]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)  
