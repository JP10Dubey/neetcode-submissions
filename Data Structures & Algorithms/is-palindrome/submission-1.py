class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        length = len(s)
        for l in range (length//2):
            if s[l].lower() != s[length-1-l].lower():
                return False
        return True

        