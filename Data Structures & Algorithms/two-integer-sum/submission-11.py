class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = {}

        for i in range(len(nums)):
            nums_hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_hashmap and i != nums_hashmap[diff]:
                return [i, nums_hashmap[diff]]