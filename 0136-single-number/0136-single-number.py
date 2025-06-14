class Solution(object):
    def singleNumber(self, nums):
        a = {}
        for num in nums:
            if num not in a:
                a[num] = 1
            else:
                a[num] += 1
        for num in nums:
            if a[num] == 1:
                return num
