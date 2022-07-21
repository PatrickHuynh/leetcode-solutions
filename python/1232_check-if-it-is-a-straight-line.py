class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        dy = (coordinates[1][1] - coordinates[0][1])
        dx = (coordinates[1][0] - coordinates[0][0])
        is_vertical = False
        grad = None
        if dx == 0:
            is_vertical = True
        else:
            grad = dy/dx
        for i in range(2, len(coordinates)):
            dy = (coordinates[i][1] - coordinates[i-1][1])
            dx = (coordinates[i][0] - coordinates[i-1][0])
            if dx == 0:
                if not is_vertical:
                    return False
                continue
            else: # dx != 0
                if grad != dy/dx:
                    return False
        return True