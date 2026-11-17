class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        i = 0 
        max = 1 
        curr = 1
        while i < len(nums) - 1:
            j = i + 1
            diff = nums[j] - nums[i]
            if diff == 0:
                i += 1
                continue
            if diff == 1:
                curr += 1
            else: 
                curr = 1
            if curr > max :
                max = curr
            i += 1
        return max
