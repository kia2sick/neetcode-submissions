import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        heap = []
        result = []
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1    

        for num, frequency in count.items():
            heapq.heappush(heap, (-frequency, num))

        for i in range(k):
            frequency, num = heapq.heappop(heap)
            result.append(num)
        
        return result




