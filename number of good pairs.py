class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i, j = 0, 1 # the iteration starts at i zeroo and j at one
        output = 0
        
        while i < len(nums) - 1:
            while j < len(nums):
                if nums[i] == nums[j]:
                    output += 1
                j += 1
            
            i += 1 # this increments i by one
            j = i + 1   # and this j by one but j should always be greater than i
        
        return output
      from typing import List
####################################################
# this code should also work
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i, j = 0, 1
        output = 0
        
        while i < len(nums) - 1:   # This mean i cant iterate on the last item 
            while j < len(nums):
                if nums[i] == nums[j]:
                    output += 1
                j += 1
            
            i += 1
            j = i + 1
        
        return output
