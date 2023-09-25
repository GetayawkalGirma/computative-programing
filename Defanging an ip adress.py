class Solution:
    def defangIPaddr(self, address: str) -> str:
        target="."
        dot="[.]"
        output=""
        for word in address:
            if word!=target:
                output+=word
            else:
                output+=dot
                
        return output
