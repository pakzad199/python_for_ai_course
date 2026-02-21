# class Math:
#     x = 0
#     y = 0

#     def sum(self):
#         return self.x + self.y
    
# math1 = Math()
# input1 = int(input("Enter first number: "))
# input2 = int(input("Enter second number: "))

# math1.x = input1
# math1.y = input2

# result = math1.sum()
# print("result: ", result)




class car:
    tire = 0
    capacity = 0
    color = None
    engine = None

    def __init__(self, tire, capacity, color, engine):
        self.tire = tire
        self.capacity = capacity
        self.color = color
        self.engine = engine
        


class Prid(car):
    brand = None

    def setBrand(self, brand):
        self.brand = brand

    def getBrand(self):
        return self.brand



# base_car = car(4, 5, 'white', 'p111')

p = Prid(4, 5, 'white', 'p111')
p.setBrand('132')
p.brand = '111'


print(p.brand)