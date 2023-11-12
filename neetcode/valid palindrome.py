class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        alphabet=''
        for char in s:
            if char.isalnum():
                alphabet +=char
        l,r=0,len(alphabet)-1
        while l<r:
            if alphabet[l]==alphabet[r]:
                l+=1
                r-=1               
            else:
                return False
        return True
