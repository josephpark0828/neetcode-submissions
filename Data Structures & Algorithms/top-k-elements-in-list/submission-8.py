class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        keys_list = list(sorted_counts.keys())
        return keys_list[0:k]