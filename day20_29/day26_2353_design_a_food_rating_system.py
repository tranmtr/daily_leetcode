from typing import List


# class FoodRatings:

#     def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
#         self.food_cuisines = dict()
#         self.food_ratings = dict()
#         self.cusines_food_max = dict()
#         n = len(foods)
#         for i in range(n):
#             self.food_cuisines[foods[i]] = cuisines[i]
#             self.food_ratings[foods[i]] = ratings[i]
#             if (cuisines[i] not in self.cusines_food_max):
#                 self.cusines_food_max[cuisines[i]] = (foods[i], ratings[i])
#             else:
#                 pair = self.cusines_food_max[cuisines[i]]
#                 if (pair[1] < ratings[i] or (pair[1] == ratings[i] and pair[0] > foods[i])):
#                     self.cusines_food_max[cuisines[i]] = (foods[i], ratings[i])
#         print(self.food_cuisines)
#         print(self.food_ratings)
#         print(self.cusines_food_max)

#     def changeRating(self, food: str, newRating: int) -> None:
#         self.food_ratings[food] = newRating
#         tmp_cuisine = self.food_cuisines[food]
#         pairOld = self.cusines_food_max[tmp_cuisine]

#         if (pairOld[0] == food):
#             self.cusines_food_max[tmp_cuisine] = (food, newRating)
#             if (pairOld[1] > newRating):
#                 minNameFood = "zzzzzzzzzzzz"
#                 maxRating = 0
#                 for x in self.food_cuisines:
#                     if (self.food_cuisines[x] == tmp_cuisine):
#                         rating = self.food_ratings[x]
#                         if (rating > maxRating or (rating == maxRating and x < minNameFood)):
#                             maxRating = rating
#                             minNameFood = x
#                 self.cusines_food_max[tmp_cuisine] = (minNameFood, maxRating)
#         else:
#             if (pairOld[1] > newRating):
#                 return
#             elif (pairOld[1] == newRating):
#                 if (pairOld[0] > food):
#                     self.cusines_food_max[tmp_cuisine] = (food, newRating)
#             else:
#                 self.cusines_food_max[tmp_cuisine] = (food, newRating)
  
#     def highestRated(self, cuisine: str) -> str:
#         return self.cusines_food_max[cuisine][0]

import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_ratings = dict()
        self.food_cuisines = dict()
        self.cuisines_rating_food = dict()
        n = len(foods)
        for i in range(n):
            self.food_cuisines[foods[i]] = cuisines[i]
            self.food_ratings[foods[i]] = ratings[i]
            if (cuisines[i] not in self.cuisines_rating_food):
                self.cuisines_rating_food[cuisines[i]] = []
            heapq.heappush(self.cuisines_rating_food[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating
        heapq.heappush(self.cuisines_rating_food[self.food_cuisines[food]], (-newRating, food))
        return
    
    def highestRated(self, cuisine: str) -> str:
        while (True):
            heap = self.cuisines_rating_food[cuisine]
            max_rating = -heap[0][0]
            food = heap[0][1]
            if (self.food_ratings[food] == max_rating):
                return food
            else:
                heapq.heappop(self.cuisines_rating_food[cuisine])

inp = [["kimchi","miso","sushi","moussaka","ramen","bulgogi"],["korean","japanese","japanese","greek","japanese","korean"],[9,12,8,15,14,7]]
S = FoodRatings(inp[0], inp[1], inp[2])










# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)