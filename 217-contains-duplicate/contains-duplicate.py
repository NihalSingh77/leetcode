#44.ContainsDuplicate
class Solution(object):
    def containsDuplicate(self, nums):
        hash_table = {}
        for p in range(len(nums)):
            if hash_table.get(nums[p]):
                return True
            else:
                hash_table[nums[p]] = True
        return False
