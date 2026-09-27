class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_length = 0

        for num in numbers:
            if num - 1 not in numbers:
                length = 1
                current = num
                while True:
                    if  current + 1 in numbers:     
                        length += 1
                        current = current + 1
                    else:
                          max_length = max(max_length, length)
                          break
        
        return max_length         