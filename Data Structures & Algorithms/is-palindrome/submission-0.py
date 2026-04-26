class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''.join(c for c in s if c.isalnum())
        text = text.lower()

        left = 0
        right = len(text)-1

        while right > left:
            if text[left] != text[right]:
                return False

            left += 1
            right -= 1

        return True