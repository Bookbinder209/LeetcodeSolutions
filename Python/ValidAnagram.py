class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        dictS = {}
        dictT = {}
        for c in s:
            if c not in dictS:
                dictS[c] = 1
            else:
                dictS[c] += 1
        
        for c in t:
            if c not in dictT:
                dictT[c] = 1
            else:
                dictT[c] +=1

        return dictS == dictT


                

            
