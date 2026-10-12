class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = {}
        for indx, i in enumerate(nums):
            dif = target - i
            if dif in new:
                return [new[dif], indx]
            new[i] = indx
        return