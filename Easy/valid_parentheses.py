class Solution:
    def isValid(self, s: str) -> bool:
        brkt = ['(', ')', '[', ']', '{', '}']
        for i in range(len(s)):
            if s[0] == brkt[0] and s[1] == brkt[1]:
                return True
            else:
                return False


a = Solution()

print(a.isValid("{[]}"))