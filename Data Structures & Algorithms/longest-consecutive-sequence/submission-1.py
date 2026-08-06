class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}

        count = 0
        count_list = []

        for i, num in enumerate(nums):
            nums_dict[i] = num

        for num in nums:
            if num - 1 not in nums_dict.values():
                count = 1
                next_num = num + 1
                
                while next_num in nums_dict.values():
                    count += 1
                    next_num += 1

                count_list.append(count)
            
        if len(count_list) > 0:
            return max(count_list)
        return 0