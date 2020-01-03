class Car :
    def __init__(self, 제조사, 모델, 색상):
        self.제조사 = 제조사
        self.모델 = 모델
        self.색상 = 색상
        self.기름양 = 1000

    def forward(self):
        self.기름양 = self.기름양-50
        print(self.제조사, self.모델, self.색상, "차량 전진중입니다! 현재 기름양 :", self.기름양, "입니다")
    def reverse(self):
        self.기름양 = self.기름양-30
        print(self.제조사, self.모델, self.색상, "차량 후진중입니다! 현재 기름양 :", self.기름양, "입니다")

class ElectricCar(Car) :

    def __init__(self):(self, 제조사, 모델, 색상) :
        super().__init__(제조사, 모델, 색상)
        self.battery = 100)

    def forward(self):
        self.battery = self.battery-10
        print(self.제조사, self.모델, self.색상, self.battery, "%입니다")
    def reverse(self):
        self.battery = self.battery-5
        print(self.제조사, self.모델, self.색상, self.battery, "%입니다")


Car1 = Car("Hyundai", "제네시스", "Black")
Car2 = Car("BMW", "720i", "Green")
Car3 = Car("Kia", "stinger", "Yellow")

Car1.forward()
Car2.reverse()
Car3.forward()
Car1.reverse()
Car1.forward()

ElectricCar1. forward()
ElectricCar2.reverse()
ElectricCar3.reverse()
