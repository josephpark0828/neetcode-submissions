class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_nums:
                return [prev_nums[diff], i]
            prev_nums[n] = i