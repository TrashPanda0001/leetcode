import copy
class Solution(object):
    def __init__(self):
        self.answers = []

    def isPalindrome(self,s):
        left = 0 
        right = len(s)-1
        while(left<right):
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def getPalindromicPartitions(self,s,partitions):
        if len(s)==0:
            self.answers.append(copy.deepcopy(partitions))
        for i in range(0,len(s)):
            substr = s[0:i+1]
            string_left = s[i+1:]
            if self.isPalindrome(substr):
                partitions.append(substr)
                self.getPalindromicPartitions(string_left,partitions)
                partitions.pop()

    def partition(self, s):
        self.getPalindromicPartitions(s,[])
        return self.answers


s = input("enter string")
solution = Solution()
print(solution.partition(s))