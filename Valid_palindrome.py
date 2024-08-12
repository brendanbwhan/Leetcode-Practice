import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        clean_s = s.lower()

        l_pointer = 0  # Start from the first character
        r_pointer = len(clean_s) - 1  # Start from the last character

        while l_pointer <= r_pointer:
            if clean_s[l_pointer] == clean_s[r_pointer]:
                l_pointer += 1
                r_pointer -= 1
            else:
                return False

        return True
