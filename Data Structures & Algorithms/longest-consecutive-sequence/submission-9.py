class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)

        for num in nums_set:
            next_num = num + 1
            count = 1
            while next_num in nums_set:
                count += 1
                next_num += 1
            res = max(res, count)
        
        return res