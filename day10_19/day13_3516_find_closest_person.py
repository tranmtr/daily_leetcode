class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distanceXtoZ = abs(x - z)
        distanceYtoZ = abs(y - z)
        if (distanceXtoZ < distanceYtoZ):
            return 1
        elif (distanceXtoZ > distanceYtoZ):
            return 2
        return 0
