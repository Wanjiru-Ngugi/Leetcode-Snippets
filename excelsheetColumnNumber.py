class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Iterartive approach
        ans = 0
        index = 0
        while index < len(s):
            power = len(s) - index - 1
            ans = ans + 26**(power) * (ord(s[index]) - 64)
            index += 1
        return ans
    
    def titleToNumberRecursive(self, s):
        """
        :type s: str
        :rtype: int
        """    
        # Recursive approach        
        if len(s) == 1:
            return ord(s[0]) - 64
        return (ord(s[0]) - 64) * 26 **(len(s)-1) + self.titleToNumber(s[1:])