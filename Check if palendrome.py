class Solution:
    def isPalindrome(self, x: int) -> bool:
    

# Convert the number to a string to extract digits
        x_str = str(x)

# Initialize an empty list to store the digits
        digits_list = []

# Iterate through each character (digit) and append it to the list
        for digit_char in x_str:
            if digit_char.isdigit():
                digits_list.append(int(digit_char))
            else:
                return False

# Reverse the list using reversed()
        reversed_digits = list(reversed(digits_list))

# Compare the original list and the reversed list
        if digits_list == reversed_digits:
            return True
        else:
            return False

        

            
        
