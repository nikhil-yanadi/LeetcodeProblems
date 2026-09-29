class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        max_d=0
        for i in s:
            if(i=="("):
                count+=1
                max_d=max(max_d,count)
            elif(i==")"):
                count-=1
        return max_d
        