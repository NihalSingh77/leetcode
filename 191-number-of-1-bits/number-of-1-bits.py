#39.NumberOf1Bits
class Solution(object):
    def hammingWeight(self, n):
        count = Counter(bin(n))
        return count["1"]
        