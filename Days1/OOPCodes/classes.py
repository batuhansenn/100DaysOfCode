# classes
class Employee(object):
    # attribute = age, address, name
    # behavior = pass
    pass

employee1 = Employee()

##############################################################################################################

# attribute
class Footballer:
    football_club = "Fenerbahce"
    age = 30
    
f1 = Footballer()

#print(f1)
#print(f1.age)
#print(f1.football_club)

f1.football_club = "Goztepe"

#print(f1.football_club)

##############################################################################################################

# methods
class Square(object):
    edge = 5 #attribute
    area = 0
    
    def area1(self):
        self.area = self.edge * self.edge 
       # print("Area: ",self.area)
        
s1 = Square()
#print(s1)
#print(s1.edge)
#print(s1.area())

s1.edge = 7
s1.area1()
#print(s1.edge)

##############################################################################################################

# methods vs function

class Emp(object):
    
    age = 25
    salary = 1000
    
    def ageSalaryRatio(self):
        return self.age / self.salary
        
e1 = Emp()
e1.ageSalaryRatio()

#print(e1.ageSalaryRatio())


# function
def ageSalaryRatio(age, salary):
    a = age / salary
    #print("Function: ", a)

ageSalaryRatio(25, 1000)


def findArea(a, b) :
    area = a*b**2
    # print(area)
    return area 
    
pi = 3.14
r = 5

result1 = findArea(pi, r)
result2 = findArea(pi, 10)

#print(result1 + result2)

##############################################################################################################

# initializer or constructor
class Animal(object):

    def __init__(self, name, age): # (name, age) = ("dog", 2) = (a, b)
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
a1 = Animal("dog", 2)
a2 = Animal("cat", 3)
a3 = Animal("bird", 1)

