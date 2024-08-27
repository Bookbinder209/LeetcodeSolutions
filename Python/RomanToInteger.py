class Solution(object):
    def romanToInt(self, s):

        
        romanDict = {"I" : 1, "V" : 5, "X" : 10, "IV" : 3, "IX" : 8,
        "L" : 50, "C" : 100, "XL" : 30, "XC" : 80,
        "D" : 500, "M" : 1000, "CD" : 300, "CM" : 800 }

        subString = ""
        answer = 0


        for count, item in enumerate(s):
            subString += item
            if subString in romanDict:
                answer += romanDict[subString]
            else:
                subString = item
                answer += romanDict[subString]
        
        return answer

