class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = {}

        for i in range(len(nums)):
            nums_hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in nums_hashmap and i != nums_hashmap[target - nums[i]]:
                return [i, nums_hashmap[target - nums[i]]]