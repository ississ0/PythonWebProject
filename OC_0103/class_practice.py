# Human이라는 Class가 있고
# 그 Class를 이용하여 김도한이라는 Object를

class Human:
    # __init__ 함수는 Constructor입니다.
    # Constructor를 이용하여 Object를 만들 수 있습니다.
    def __init__(self, name, age, gender, height, blood):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.blood = blood

    def introduceMySelf(self):
        print ("제 이름은", self.name, "이고 나이는", self.age, "입니다.")

eunjeenRyu=Human("류은진", 35, "Female", 167, "A")
dohanKim=Human("김도한", 20, "Male", 179, "AB")
yoosunJeong=Human("정유선", 31, "Female", 168, "O")

eunjeenRyu.introduceMySelf()
dohanKim.introduceMySelf()
yoosunJeong.introduceMySelf()

