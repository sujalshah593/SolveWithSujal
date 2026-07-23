from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums.reverse()

        left,right = 0, k-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        #Reverse remaining 
        left, right = k, n -  1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

n = Solution()
nums = [1,2,3,4,5,6,7] 
k = 3
n.rotate(nums, k)
print(nums)