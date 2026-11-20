class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                if arr[i] > max:
                    tmp = arr[i]
                    arr[i] = max
                    max = tmp
                else:
                    arr[i] = max
        return arr
