class Solution(object):
    def isPalindrome(self, s):
        s = s.replace(" ", "")
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        right = len(s) - 1
        for i in range(len(s)):
            if s[i] == s[right]:
                right -= 1
            else:
                return False
        return True
    