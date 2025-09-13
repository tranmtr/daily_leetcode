class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = set('aeiou')
        dict_alphabet = {}
        for x in s:
            if x in dict_alphabet:
                dict_alphabet[x] += 1
            else:
                dict_alphabet[x] = 1

        max_vowel = 0
        max_consonant = 0
        for key in dict_alphabet:
            if key in vowel:
                if dict_alphabet[key] > max_vowel:
                    max_vowel = dict_alphabet[key]
            else:
                if dict_alphabet[key] > max_consonant:
                    max_consonant = dict_alphabet[key]

        return max_consonant + max_vowel
            

s = "successes"
S = Solution()
print(S.maxFreqSum(s))
