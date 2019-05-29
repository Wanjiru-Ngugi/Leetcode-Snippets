class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """        
        # Number Implementation till half the number
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10
        return x == reverse or x == reverse // 10

    def isPalindromeString(self, x):
        """
        :type x: int
        :rtype: bool
        """    
        # String Implementation
        y = str(x)
        for c in range(len(y)):
            d = len(y) - c -1
            if y[c] != y[d]:                
                return False
            if d <= c:
                return True
    

    def isPalindromeNumber(self, x):
        """
        :type x: int
        :rtype: bool
        """                
        # Number Implementation
        if x < 0:
            return False
        else:
            return self.reverse(x) == x
    
    def reverse(self, x):
        reverse = 0
        
        while x >  0:
            temp = x % 10
            reverse = reverse * 10 + temp
            x = x // 10
        return reverse
        