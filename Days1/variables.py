#Variables(Degiskenler)

var1 = 15 #integer
var2 = 20 #integer
day = "monday" #string
var3 = 15.5 #float
var4 = 25
var5 = 25


#String
variable_type = type(day)
print(day)
print(type(day))
str1 = "100" #string not integer
str2 = "200" # str not int
print(variable_type)


#numbers
b = 10.5 #float or double
c = -15 
d = -15.5


#Built in Functions
strNew = "1000" #not int - string
print(strNew) 
type(strNew) 
newInt = int(strNew)
type(newInt)
pi = 3.14
e = 2.71


#Default and flexible functions
def circle():
    pi = 3.14
    r = float(input("Enter radius: "))

    area = pi * r * r

    print("Area of circle is: ", area)
    
    return area

print(circle())


def hesapla (boy, kilo, *args):
    print (args)

    output = (boy+kilo)*args[0]
    return output

print(hesapla(180, 75, 10))

#lambda function 
def calculate(x):
    return 2 * x + 5    
result1 = calculate(5)
print(result1)
    
result2 = lambda x : 2 * x + 5 

print(result2(5))   

#list
#          3  -2  -1
list1 = [1,2,3,4,5,6]
#        0 1 2 3 4 5
list_str = ["one","two","three"]

type(list1)

value = list1[-2]

print(list1[-2])

dividedList = list1[0:3]  # in math :[0:3)

dir(list)

list1.append(7)
list1.remove(7)
list1.reverse()

list2 = [4,5,3,1,2,6]

list2.sort()
    
lis3 = [1,2,3,"a","b","c"]
    
#tuple
tuple1 = (1,2,3,3,4,5,6)

tuple1[2]

tuple1.count(3)


#dictionary
dict1 = {"jeff":30,"jack":25,"ally":31}

#keys : jeff jack and ally
#values: 30 25 and 31

type(dict1["jeff"])


dict1.values()

def dictcreater():
    dictionary = {"jeff":35,"jack":35,"ally":45}
    
    return dictionary

newDict = dictcreater()


#if else statements

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 is greater than var2")
elif(var1 ==var2):
    print("var1 is equal to var2")
else:
    print("var2 is greater than var1")
    

list1 = [0,1,2,3,4]

value = 6

if value in list1:
    print("{} is in the list".format(value))
else:
    print("{} is not in the list".format(value))
    

keys = dict1.keys() 

if "asd" in keys:
    print("true")
else:
    print("false")


# for loop

for numbers in range(1,11):
    print(numbers)
    
    
for letters in "new york":
    print(letters)



for letters in "new york".split():
    print(letters)



list1 = [1,2,3,4,5,6,]

summation1 = sum(list1)


count = 0

for numbers in list1:
    count = count + numbers
    print(count)


# while loop
    
i = 0

while(i<5):
    print(i)
    i = i + 1
    
    
limit = len(list1)    
    
index = 0

sum2 = 0

while(index<limit):

    sum2 = sum2 + list1[index]
    index = index+1    
