class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}

        count = 0
        count_list = []

        for i, num in enumerate(nums):
            nums_dict[i] = num

        for num in nums:
            if num - 1 not in nums_dict.values():  # Check if it's the start of a sequence
                count = 1  # Start counting with the current number
                next_num = num + 1

                while next_num in nums_dict.values():  # Look for consecutive numbers
                    count += 1
                    next_num += 1
                
                count_list.append(count)

        return max(count_list) if count_list else 0  # Handle empty count_list