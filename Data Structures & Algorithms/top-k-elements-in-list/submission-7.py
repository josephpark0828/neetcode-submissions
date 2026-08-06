class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create dict that holds each number and its count
        nums_counts = {}
        for num in nums:
            nums_counts[num] = nums_counts.get(num, 0) + 1
        
        # create buckets that store each number
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        # each bucket's index = each number's count
        for num, cnt in nums_counts.items():
            buckets[cnt].append(num)

        # iterate through the buckets backwards until you have k numbers
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                if len(res) != k:
                    res.append(num)
        
        return res