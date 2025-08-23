    areaAbove = self.minimumTotalTwoRec(grid[: i + 1], True)
                areaBelow = self.minimumArea(grid[i + 1 :])

                if (areaAbove + areaBelow < minTotal):
                    minTotal = areaAbove + areaBelow