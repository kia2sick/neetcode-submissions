class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        x = len(numbers)-1
        nums = []

        while i < x:
             
             if numbers[i] + numbers[x] == target:
                nums.extend([i+1, x+1])

             if numbers[i] + numbers[x] < target:
                i += 1
                continue
             else:
                x-=1
                continue 
        return nums          


        