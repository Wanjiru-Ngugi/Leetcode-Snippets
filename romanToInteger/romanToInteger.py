class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000                
               }        
        num = 0
        index = 0       
        # loop through entire string
        while index < len(s):
            currChar = s[index]
            # if we're at the last char of the string add it's corresponding value to num
            if index + 1 >= len(s):
                num += dict[currChar]
                return num
            else:
            # compare the next char to current char, if next is greater, num is num + next - curr. Move index by 2
                nextChar = s[index + 1]
                if dict[nextChar] > dict[currChar]:
                    num += dict[nextChar] - dict[currChar]
                    index += 2
                else:
                # else num is num + curr move index by 1
                    num += dict[currChar]
                    index += 1
        return num