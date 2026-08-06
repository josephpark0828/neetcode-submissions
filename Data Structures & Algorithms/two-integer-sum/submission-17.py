class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        
        for i, num in enumerate(nums):
            nums_dict[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict and i != nums_dict[diff]:
                return [i, nums_dict[diff]]