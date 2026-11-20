class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max = 0
        curr = 0
        for i, num in enumerate(nums):
            if num == 1:
                curr += 1
                if max < curr:
                    max = curr
            else:
                if max < curr:
                    max = curr
                curr = 0
        return max
