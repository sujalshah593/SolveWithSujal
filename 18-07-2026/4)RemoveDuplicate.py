from typing import List

class Solution:
    def RemoveDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return  i + 1
    
nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
result = solution.RemoveDuplicates(nums)
print(result)
print(nums[:result])  # Print the modified array up to the new length