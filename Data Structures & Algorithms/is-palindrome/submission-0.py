class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        length = len(s)
        for l in range (length//2):
            if s[l] != s[length-1-l]:
                return False
        return True

        