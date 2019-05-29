class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = {1: "I",
                5: "V",
                10: "X",
                50: "L",
                100: "C",
                500: "D",
                1000: "M"                
               }
        p = len(str(num))-1
        out = ''
        for c in str(num):
            if int(c) == 4:
                out += dict[10**p] + dict[5*(10**p)]
            if int(c) == 9:
                out += dict[10**p] + dict[10*(10**p)]
            if 0 < int(c) < 4:
                out += dict[10**p] * int(c)
            if 5 < int(c) < 9:
                out += dict[5*(10**p)] + dict[10**p] * (int(c) - 5)
            if int(c) == 5:
                out += dict[5*(10**p)]
            p -=1
        return out