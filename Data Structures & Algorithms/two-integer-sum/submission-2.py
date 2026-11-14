class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = sorted([(val, idx) for idx, val in enumerate(nums)])
        left = 0
        right = len(indexed_nums) - 1
        while left < right:
            sum = indexed_nums[left][0] + indexed_nums[right][0]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return sorted([indexed_nums[left][1], indexed_nums[right][1]])