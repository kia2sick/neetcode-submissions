class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        list = []
        nums.sort()

        for index, num in enumerate(nums):

            target = -num
            i = index + 1
            x = len(nums)-1
            while i < x:
                group = []
                if nums[i] + nums[x] == target:
                    group.extend([nums[i], nums[x], num])
                    group.sort()
                    if group not in list:
                        list.append(group)
                        i += 1
                        x -= 1
                        continue
                if nums[i] + nums[x] < target:
                    i += 1
                    continue
                else:
                    x -= 1
                    continue    
        return list




        