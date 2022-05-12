# OOP
# DRY
# attributes and methods
# parameters and arguments
# class objects attributes is static
# class objects method
# encapsulation
# abstraction
# inheritence
# polymorphism
# @classmethod, @staticmethod and @property

class ExClass:
    num1 = 11
    num2 = 7
    comment = "end of calculation"
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def adding_2_numbers(self):
        result = self.num1 + self.num2
        print(f"num1 {self.num1} is added to num2 {self.num2} resulting in {result} \n{self.comment}")

    @classmethod
    def multiply_2_numbers(cls):
        result = ExClass.num1 * ExClass.num2
        print(f"num1 {ExClass.num1} is multiplied by num2 {ExClass.num2} resulting in {result} \n{ExClass.comment}")

    @staticmethod
    def substract_2_numbers(num1, num2):
        result = num1 - num2
        print(f"num2 {num2} is substracted by num1 {num1} resulting in {result} \n {ExClass.comment}")

    @property
    def dividing_2_numbers(self):
        result = self.num1 / self.num2
        print(f"num1 {self.num1} is divded by num2 {self.num2} resulting in {result} \n{self.comment}")




instance_obj = ExClass(8, 10)
print(instance_obj.num1)
instance_obj.adding_2_numbers()
instance_obj.multiply_2_numbers()
instance_obj.substract_2_numbers(20,10)
instance_obj.dividing_2_numbers


