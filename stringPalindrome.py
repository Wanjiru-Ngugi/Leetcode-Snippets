class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'\W', '', s).upper()
        return s == s[::-1]

    def isPalindromeIterative(self, s):
        """
        :type s: str
        :rtype: bool
        """    
		# Check till half length of string        
        s = re.sub(r'\W', '', s).lower()        
        start = 0
        end = len(s)
        while start < end:
            if s[start] != s[end-1]:
                return False
            start += 1
            end -= 1
        return True
            
        