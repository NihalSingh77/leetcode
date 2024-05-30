#36.MajorityElement
class Solution(object):
    def majorityElement(self, nums):
        dupli=[]
        count1=[]
        dupli[:]=list(set(nums))
        for i in range(len(dupli)):
           count1.append( nums.count(dupli[i]))
        m=max(count1)
        for i in range(len(count1)):
            if count1[i]==m:
                p=i
                break
        return dupli[p]

            
        