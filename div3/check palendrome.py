class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        combined=""

        for letter in s:
            if letter.isalnum():
                combined+=letter
        if combined == combined[::-1]:
            return True
        else: 
            return False
