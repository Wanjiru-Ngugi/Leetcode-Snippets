class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        negFlag = False
        
        if x < 0:
            negFlag = True
            x = abs(x)
        while x > 0:
            temp = x % 10
            reverse = reverse * 10 + temp
            x = x//10
        if negFlag is True:
            reverse = reverse * -1
        if abs(reverse) > 2147483647:
            return 0
        return reverse