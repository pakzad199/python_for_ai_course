class Math:
    x = 0
    y = 0

    def sum(self):
        return self.x + self.y
    
math1 = Math()
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))

math1.x = input1
math1.y = input2

result = math1.sum()
print("result: ", result)