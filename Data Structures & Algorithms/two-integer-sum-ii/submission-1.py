class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize left and right pointers
        l = 0
        r = len(numbers) - 1

        # check if sum adds up to target
        while l < r:
            # if too big --> increment right pointer
            if numbers[l] + numbers[r] > target:
                r -= 1
            # if too small --> increment left pointer
            elif numbers[l] + numbers[r] < target:
                l += 1
            # if same --> return indices
            else:
                return [l + 1, r + 1]