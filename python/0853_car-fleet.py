class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = [[i[0], (target-i[0])/i[1]] for i in zip(position, speed)]
        data.sort(key=lambda car: car[0], reverse=True)
        fleet_ttt = 0
        fleet_count = 0 
        for i in range(0, len(data)):
            if data[i][1] > fleet_ttt:
                fleet_ttt = data[i][1]
                fleet_count += 1
        return fleet_count