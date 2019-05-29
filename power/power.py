class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1/(self.myPow(x, n*-1))
        half = self.myPow(x, n/2)
        rem = self.myPow(x, n%2)
        return half *half * rem
        

    def myPowIterative(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """   
        negFlag = False
        if n < 0:
            negFlag = True
            n = abs(n)
        ans = 1
        while n > 0:
            ans *= x
            n -= 1
        if negFlag == True:
            ans = 1/ans
        return ans      