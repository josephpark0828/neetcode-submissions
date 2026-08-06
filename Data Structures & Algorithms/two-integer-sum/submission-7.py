class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preVal = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in preVal:
                return sorted([index, preVal[diff]])
            preVal[value] = index
            