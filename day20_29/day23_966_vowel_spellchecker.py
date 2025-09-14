from typing import List


# class Solution:
#     def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
#         answer = []
#         lower_wordlist = [x.lower() for x in wordlist]
#         lower_queries = [x.lower() for x in queries]

#         vowels_mapping = {"a": "a", "e": "a", "i": "a", "o": "a", "u": "a"}

#         replace_lower_wordlist = [
#             ''.join(vowels_mapping.get(ch, ch) for ch in word)
#             for word in lower_wordlist
#         ]

#         replace_lower_queries = [
#             ''.join(vowels_mapping.get(ch, ch) for ch in word)
#             for word in lower_queries
#         ]

#         len_queries = len(queries)
#         len_wordlist = len(wordlist)

#         for i in range(len_queries):
#             flag = False            #Chua khop
#             for j in range(len_wordlist):
#                 if wordlist[j] == queries[i]:
#                     flag = True
#                     answer.append(wordlist[j])
#                     break
#             if not flag:
#                 for j in range(len_wordlist):
#                     if lower_wordlist[j] == lower_queries[i]:
#                         flag = True
#                         answer.append(wordlist[j])
#                         break
#             if not flag:
#                 for j in range(len_wordlist):
#                     if replace_lower_wordlist[j] == replace_lower_queries[i]:
#                         flag = True
#                         answer.append(wordlist[j])
#                         break
#             if not flag:
#                 answer.append("")
#         return answer

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return ''.join(['a' if x in "aeuio" else x for x in word.lower()])
        
        word_extract = set(wordlist)
        word_lowers = {}
        for word in wordlist:
            if word.lower() in word_lowers:
                continue
            word_lowers[word.lower()] = word
        
        word_replace_vowels = {}
        for word in wordlist:
            new_word = devowel(word)
            if new_word in word_replace_vowels:
                continue
            word_replace_vowels[new_word] = word

        answer = []
        for query in queries:
            if (query in word_extract):
                answer.append(query)
            elif (query.lower() in word_lowers):
                answer.append(word_lowers[query.lower()])
            elif (devowel(query) in word_replace_vowels):
                answer.append(word_replace_vowels[devowel(query)])
            else:
                answer.append("")
        return answer

S = Solution()
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

print(S.spellchecker(wordlist, queries))