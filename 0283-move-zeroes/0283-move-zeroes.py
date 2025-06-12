class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums
        