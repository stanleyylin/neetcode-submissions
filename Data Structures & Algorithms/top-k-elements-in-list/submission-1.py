class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        frequencies = Counter(nums)

        buckets = [[] for _ in range(n+1)] # index is the frequency
        
        for num, freq in frequencies.items():
            buckets[freq].append(num)

        res = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) >= k:
                    return res