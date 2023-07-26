class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(arr):
            if len(arr) < 2: # if the len of the array is less than 2 there is nothing to compare it too
                return False
            diff = arr[1] - arr[0] # first two index difference
            for i in range(2, len(arr)): #so if its longer than 2
                if arr[i] - arr[i-1] != diff: # and its new differnce is not equal to the first to index diference return false
                    return False 
            return True
        
        result = []
        for i in range(len(l)):
            subarr = sorted(nums[l[i]:r[i]+1]) # this is sclicing and in this method the end index gets excluded thats why we added one
            result.append(isArithmetic(subarr)) # so this will be our array that we will be checking 
        return result
