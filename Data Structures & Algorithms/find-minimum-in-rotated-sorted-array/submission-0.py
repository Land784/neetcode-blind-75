class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1        # min is strictly right of mid
            else:
                right = mid           # min is at mid or left of it
        return nums[left] 