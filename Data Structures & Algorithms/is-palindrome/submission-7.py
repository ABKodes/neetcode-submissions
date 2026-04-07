class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for char in s:
            if char.isalnum():
                temp.append(char)
        left,right = 0,len(temp) - 1
        while left < right:
            if temp[left].lower() != temp[right].lower():
                return False
            left += 1
            right -= 1
        return True