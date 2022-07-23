class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_available = {}
        self.parking_available[1] = big
        self.parking_available[2] = medium
        self.parking_available[3] = small

    def addCar(self, carType: int) -> bool:
        if self.parking_available[carType] > 0:
            self.parking_available[carType] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)