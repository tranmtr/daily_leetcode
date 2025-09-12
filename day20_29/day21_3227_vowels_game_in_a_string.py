class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')
        for x in s:
            if x in vowels:
                return True
        return False
            