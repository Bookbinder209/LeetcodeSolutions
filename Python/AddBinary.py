class Solution(object):
    def addBinary(self, a, b):
        

        lengthA = len(a)
        lengthB = len(b)
        carryOver = 0
        index = 1
        answer = ""
        while index <= min(lengthA,lengthB):
            binaryAdd = int(a[lengthA - index]) + int(b[lengthB-index]) + carryOver
            if binaryAdd == 3:
                answer += "1"
                carryOver = 1
            elif binaryAdd == 2:
                answer += "0"
                carryOver = 1
            elif binaryAdd == 1:
                answer += "1"
                carryOver = 0
            elif binaryAdd == 0:
                answer += "0"
            index += 1

        while carryOver == 1 or index <= max(lengthA, lengthB):
            if index <= lengthA:
                binaryAdd = int(a[lengthA - index]) + carryOver
            elif index <= lengthB:
                binaryAdd = int(b[lengthB - index]) + carryOver
            else:
                binaryAdd = carryOver
            if binaryAdd == 2:
                answer += "0"
                carryOver = 1
            elif binaryAdd == 1:
                answer += "1"
                carryOver = 0
            else:
                answer += "0"

            index += 1

        return answer[::-1]

