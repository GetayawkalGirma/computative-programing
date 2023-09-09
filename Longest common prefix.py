class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i in range(len(strs[0])): # i is letter at the first word
            for word in strs: # so for every word in string
                if i== len(word) or word[i]!= strs[0][i]:
                    return res
            res += strs[0][i]
        return res
