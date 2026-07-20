from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_seen = set()
        for num in nums:
            if num in num_seen:
                return True
            num_seen.add(num)
        return False
    
nums = [1, 2, 3, 4, 5, 1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)