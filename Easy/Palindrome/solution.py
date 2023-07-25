class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Reverse the string and store in right
        right = str(x)[:: -1]
        # compare and return bool
        return str(x) == right