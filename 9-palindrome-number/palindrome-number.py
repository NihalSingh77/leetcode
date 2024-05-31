#2Palindromenumber
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        originalX = x
        numReversed = 0
        while x > 0:
            lastdigit = x % 10
            numReversed = numReversed * 10 + lastdigit
            x = x // 10
        return numReversed == originalX 
    
        