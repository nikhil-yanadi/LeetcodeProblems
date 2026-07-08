class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr=[]
        for num in nums:
            for i in str(num):
                arr.append(int(i))
        return arr
        