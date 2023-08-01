class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        output=[]
        for key,v in sorted(count.items(), key=lambda x:x[1],reverse=True):
            output.append(key)
        return output[:k]
        
