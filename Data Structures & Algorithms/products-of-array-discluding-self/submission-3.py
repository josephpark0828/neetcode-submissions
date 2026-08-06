class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        leftprod = 1
        for i in range(len(nums)):
            res[i] = leftprod
            leftprod *= nums[i]
        
        rightprod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rightprod
            rightprod *= nums[i]
        
        return res