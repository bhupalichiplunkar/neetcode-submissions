class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            if n not in indices:
                indices[n] = [i]
            else:
                indices[n].append(i)

        i = 0
        while i < len(nums):
            diff = target - nums[i]
            if diff in indices:
                for j in indices[diff]:
                    if i != j:
                        return [i, j]
            i += 1

        return []
