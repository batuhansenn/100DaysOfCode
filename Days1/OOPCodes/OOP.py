#Class and Constructor

class custumer:
    
    rais_rate = 1.8
    counter = 0
    
    def __init__(self, name, surname, age, phone, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        self.phone = phone
   
        custumer.counter = custumer.counter + 1
        
    def giveNameSurname(self):
        return self.name + " " + self.surname
    
    def insert(self):
        self.salary = self.salary * self.rais_rate
    
#
#print(custumer1.name, custumer1.surname, custumer1.age, custumer1.phone)
#print(custumer1.giveNameSurname())

##############################################################################################################

#Class variables

custumer1 = custumer("Johny", "Aga", 21, "123456789", 10000,)
custumer2 = custumer("Ayşe", "Hanim", 21, "123456789", 10000,)
#print(custumer1.salary)
#custumer1.insert()
#print("New salary: ", custumer1.salary)
#print(custumer.counter)

##############################################################################################################

#Class Example

custumer3 = custumer("Batuhan", "Şen", 19, "123456789", 35000,)
custumer4 = custumer("Elif", "Şen", 21, "123456789", 3500,)

list = [custumer1, custumer2, custumer3, custumer4]
maxi_price = -1

for each in list:
    if(each.salary > maxi_price):
        maxi_price = each.salary
        name = each.giveNameSurname()
        
print("The most expensive product: ", name, maxi_price)

