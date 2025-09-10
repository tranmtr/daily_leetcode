from typing import List
import time

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        num_lang = n
        num_user = len(languages)
        num_friendships = len(friendships)

        languages.insert(0, [])
        needs_teaching_candidates = set()
        
        for i in range(num_friendships):
            a = friendships[i][0]
            b = friendships[i][1]
            intersection = list(set(languages[a]) & set(languages[b]))
            if (intersection == []):
                needs_teaching_candidates.add(a)
                needs_teaching_candidates.add(b)
        
        languages_candidates_knows = [0 for _ in range(num_lang + 1)]
        for x in needs_teaching_candidates:
            num_lang_candidates_x_knows = len(languages[x])
            for j in range(num_lang_candidates_x_knows):
                languages_candidates_knows[languages[x][j]] += 1
        max_lang_candidates_know = 0
        for k in range(1, num_lang + 1):
            if (max_lang_candidates_know < languages_candidates_knows[k]):
                max_lang_candidates_know = languages_candidates_knows[k]
        return len(needs_teaching_candidates) - max_lang_candidates_know
        


S = Solution()
n = 17
languages = [[4,7,2,14,6],[15,13,6,3,2,7,10,8,12,4,9],[16],[10],[10,3],[4,12,8,1,16,5,15,17,13],[4,13,15,8,17,3,6,14,5,10],[11,4,13,8,3,14,5,7,15,6,9,17,2,16,12],[4,14,6],[16,17,9,3,11,14,10,12,1,8,13,4,5,6],[14],[7,14],[17,15,10,3,2,12,16,14,1,7,9,6,4]]
friendships = [[4,11],[3,5],[7,10],[10,12],[5,7],[4,5],[3,8],[1,5],[1,6],[7,8],[4,12],[2,4],[8,9],[3,10],[4,7],[5,12],[4,9],[1,4],[2,8],[1,2],[3,4],[5,10],[2,7],[1,7],[1,8],[8,10],[1,9],[1,10],[6,7],[3,7],[8,12],[7,9],[9,11],[2,5],[2,3]]
print(S.minimumTeachings(n, languages, friendships))


