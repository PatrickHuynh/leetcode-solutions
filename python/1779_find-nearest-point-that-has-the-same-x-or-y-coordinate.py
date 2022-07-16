class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        sol = -1
        dist = inf
        for i in range(len(points)):
            is_valid = points[i][0] == x or points[i][1] == y
            if is_valid:
                mdist = abs(points[i][0] - x) + abs(points[i][1] - y)
                if mdist < dist:
                    sol = i
                    dist = mdist
        return sol
        