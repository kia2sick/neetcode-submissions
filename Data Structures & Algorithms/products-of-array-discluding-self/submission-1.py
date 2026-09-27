class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
             mult = [0]*len(nums)
             i = 0
             while i < len(nums):
                 if i == 0:
                     prev_number = 1 
                
                 mult[i] = prev_number
                 prev_number = prev_number * nums[i]
                 i += 1   

             i = i-1
             while i >= 0:
                 if i == (len(nums)-1):
                    prev_number = 1

                 mult[i] = mult[i] * prev_number
                 prev_number = prev_number * nums[i]
                 i -= 1

             for i in range(len(nums)):
                nums[i] = mult[i]
            
             return nums            
                  


            