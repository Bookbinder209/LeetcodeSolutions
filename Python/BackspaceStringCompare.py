class Solution(object):
    def backspaceCompare(self, s, t):

        stringS = ""
        stringT = ""

        for item in s:
            if item == "#":
                stringS = stringS[:-1]
            else:
                stringS += item

        for item in t:
            if item == "#":
                stringT = stringT[:-1]
            else:
                stringT += item

        return stringS == stringT