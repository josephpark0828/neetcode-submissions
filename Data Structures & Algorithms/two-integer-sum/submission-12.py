class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = {}

        for i, n in enumerate(nums):
            nums_hashmap[n] = i
        
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in nums_hashmap and i != nums_hashmap[diff]:
                return [i, nums_hashmap[diff]]