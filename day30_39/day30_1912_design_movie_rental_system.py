# import heapq
# from turtle import delay
# import time
# from typing import List

# class MovieRentingSystem:

#     def __init__(self, n: int, entries: List[List[int]]):
#         self.movie_queue_price_shop = dict()              #{movie: priority_queue(price, shop)}
#         self.movie_set_shop = dict()                        #{movie: set(shop)}
#         self.dict_shop_movie_price = dict()    #{(shop, movie): price}
#         self.rented = []                        #(price, shop, movie)

#         for entry in entries:
#             shop, movie, price = entry[0], entry[1], entry[2]
#             if (movie not in self.movie_queue_price_shop):
#                 self.movie_queue_price_shop[movie] = []
#                 self.movie_set_shop[movie] = set()
#             heapq.heappush(self.movie_queue_price_shop[movie], (price, shop))
#             self.movie_set_shop[movie].add(shop)
#             self.dict_shop_movie_price[(shop, movie)] = price
#         print(self.movie_queue_price_shop)
#         print()
#         print(self.movie_set_shop)
#         print()
#         print(self.dict_shop_movie_price)

#     def search(self, movie: int) -> List[int]:
#         print("SEARCH")
#         result = []
#         tmp = []
#         if movie not in self.movie_queue_price_shop:
#             return []

#         while (self.movie_queue_price_shop[movie]):
#             shop = self.movie_queue_price_shop[movie]
#             print(shop)
#             if (len(result) == 5):
#                 # print("DAY")
#                 for x in tmp:
#                     heapq.heappush(self.movie_price_shop[movie], x)
#                 return result
#             print("shop[0][1] = ", shop[0][1])
#             print("result = ", result)
#             print("set = ", self.movie_set_shop[movie])
#             print(shop[0][1] in self.movie_set_shop[movie])
#             print(shop[0][1] not in result)
#             if (shop[0][1] in self.movie_set_shop[movie] and shop[0][1] not in result):
#                 # print("HHHEHEHEHEHEH")
#                 print("VAO")
#                 result.append(shop[0][1])
#                 tmp.append(shop[0])
#                 # print(self.movie_queue_price_shop[movie])
#             heapq.heappop(self.movie_queue_price_shop[movie])
#             # print("NGOAI")
#             time.sleep(0.5)
#         for x in tmp:
#             heapq.heappush(self.movie_queue_price_shop[movie], x)
#             # print("NE")
#         return result
    
#     def rent(self, shop: int, movie: int) -> None:
#         print("RENT")
#         self.movie_set_shop[movie].discard(shop)
#         price = self.dict_shop_movie_price[(shop, movie)]
#         self.rented.append((price, shop, movie))
#         print(self.rented)
#         self.rented.sort()
#         if (len(self.rented) > 5):
#             self.rented.pop()

#     def drop(self, shop: int, movie: int) -> None:
#         print("DROP")
#         self.movie_set_shop[movie].add(shop)
#         price = self.dict_shop_movie_price[(shop, movie)]
#         heapq.heappush(self.movie_queue_price_shop[movie], (price, shop))
#         if ((price, shop, movie) in self.rented):
#             self.rented.remove((price, shop, movie))
        

#     def report(self) -> List[List[int]]:
#         print("REPORT")
#         result = []
#         for x in self.rented:
#             result.append([x[1], x[2]])
#         return result

# n = 3
# entries = [[4,374,55],[1,6371,21],[8,3660,24],[1,56,32],[5,374,71],[3,4408,36],[6,9322,73],[6,9574,92],[8,7834,62],[2,6084,27],[7,3262,89],[2,8959,53],[0,3323,41],[6,6565,45],[0,4239,20]]
# S = MovieRentingSystem(n, entries)
# print(S.rent(0, 4239))
# print(S.drop(0, 4239))
# print(S.rent(3, 4408))
# print(S.rent(2, 6084))
# print(S.rent(0, 4239))
# print(S.drop(0, 4239))
# print(S.search(9346))
# print(S.report())
# print(S.rent(6, 9322))
# print(S.search(8698))

import heapq
from typing import List

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented_movies = {}
        self.movie_prices = {}
        self.rented_movies_heap = []
        self.rented_set = set()

        for shop, movie, price in entries:
            if movie not in self.unrented_movies:
                self.unrented_movies[movie] = []
            heapq.heappush(self.unrented_movies[movie], (price, shop))
            self.movie_prices[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self.unrented_movies:
            return []
        
        heap = self.unrented_movies[movie]
        result_shops = []
        seen_shops = set()
        popped_items = []
        
        while heap and len(result_shops) < 5:
            price, shop = heapq.heappop(heap)
            popped_items.append((price, shop))
            
            if (shop, movie) in self.rented_set or shop in seen_shops:
                continue
                
            result_shops.append(shop)
            seen_shops.add(shop)
        
        for item in popped_items:
            heapq.heappush(heap, item)
            
        return result_shops

    def rent(self, shop: int, movie: int) -> None:
        price = self.movie_prices.get((shop, movie))
        if price is not None:
            self.rented_set.add((shop, movie))
            heapq.heappush(self.rented_movies_heap, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        if (shop, movie) in self.rented_set:
            self.rented_set.remove((shop, movie))

    def report(self) -> List[List[int]]:
        heap = self.rented_movies_heap
        result = []
        seen_rentals = set()
        popped_items = []
        
        while heap and len(result) < 5:
            price, shop, movie = heapq.heappop(heap)
            popped_items.append((price, shop, movie))
            
            if (shop, movie) not in self.rented_set or (shop, movie) in seen_rentals:
                continue

            result.append([shop, movie])
            seen_rentals.add((shop, movie))

        for item in popped_items:
            heapq.heappush(heap, item)
            
        return result