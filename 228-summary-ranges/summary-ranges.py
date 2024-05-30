#49.SummaryPages
class Solution(object):
    def summaryRanges(self, nums):
        res = []
        if not nums: return []
        a, b = nums[0], nums[0]

        def construct(a, b):
            if a == b:
                return str(a)
            else:
                return str(a) + "->" + str(b)

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                res.append(construct(a,b))
                a = nums[i]
                b = nums[i]
            else:
                b = nums[i]
        res.append(construct(a,b))
        return res