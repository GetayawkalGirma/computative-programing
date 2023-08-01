    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr)
        N=len(arr)
        removed_count =0 #removed count
        output=0 #means the no of pairs we remove
        for k,v in sorted(count.items(), key =lambda x:-x[1]):
            #for every key and value in the sorted count that is sorted in decreasing order 
            removed_count+=v # add the value (no of repition) for that key in n ie: the largest one  
            output+=1 # it means now you removed one item 
            if removed_count >= (N//2):
                break # when the removed count is greater than the len break
        return output

