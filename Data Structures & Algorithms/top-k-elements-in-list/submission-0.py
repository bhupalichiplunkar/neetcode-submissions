class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mid = defaultdict(list)
        num_count = defaultdict(int)
        op = []
        for n in nums:
            num_count[n] += 1
        for key, value in num_count.items():
            mid[value].append(key)
        i = len(nums)
        while i > 0:
            for j in mid[i]:
                op.append(j)
                if len(op) == k:
                    return op
            i -= 1
        return op
                
            
        
            

