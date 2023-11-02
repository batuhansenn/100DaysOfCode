#calculator project

class Calculator(object):
    
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b
        
    def add(self):
        return self.value1 + self.value2
    
    def multiply(self):
        return self.value1 * self.value2
    
    def division(self):
        return self.value1 / self.value2
    
    def subtraction(self):
        return self.value1 - self.value2
    
print("Choose add(1), multiply(2), division(3), subtraction(4)")
selection = input("select 1 or 2 or 3 or 4: ")

v1 = int(input("first value: "))
v2 = int(input("second value: "))

c1 = Calculator(v1,v2)
if selection == "1":
    add_result = c1.add()
    print("Add: {}".format(add_result))
elif selection == "2": # else if = elif
    multiply_result = c1.multiply()
    print("Multiply: {}".format( multiply_result))
elif selection == "3":
    div_result = c1.division()
    print("Div: {}".format(div_result))
elif selection == "4":
    sub_result = c1.subtraction()
    print("Sub: {}".format(sub_result))
else: 
    print("Error there is no proper selection")