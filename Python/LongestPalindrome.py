class Solution(object):
    def longestPalindrome(self, s):

        count = 0
        charCount = {}
        oddCount = False
        for char in s:
            charCount[char] = charCount.get(char, 0) + 1
        
        for key in charCount:

            count += charCount[key] // 2 *2
            
            if charCount[key] % 2 == 1:
                oddCount = True
                
                
        if oddCount == True:
            count += 1

        return count




             
