class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indxi, i in enumerate(nums):
            for indxj, j in enumerate(nums):
                if i+j == target and indxi!=indxj:
                    return [indxi, indxj]