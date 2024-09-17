import math

num = 2
string = "This is a test"
flag = False
shoppingList = ['Oranges', 'Garlic','Milk']
candidateData = {
    'name': 'Jesus',
    'lastname': 'Barajas',
    'age': '27',
    'employed' : 'true'
}
floatNumber= 1.2

('This', 'is','a', 'tuple', 'and', 'it is', 'inmutable') # this is a tuple, can not be modified once declared.

#lets check data types
print(type(num)) # INT
print(type(string)) #string
print(type(flag)) #boolean
print(type(shoppingList)) # list
print(type(candidateData)) #dictionary
print(type(('This', 'is','a', 'tuple', 'and', 'it is', 'inmutable'))) #tuple
print(type({3.14,12.4,11,2.5})) #Set
print(type(num+2j)) #Complex 
print(type(floatNumber)) #float


x1,y1 = 2,3
x2,y2 = 10,8


def euclideanDistance(x1, y1, x2, y2):
    euclidean = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return euclidean

print(euclideanDistance(x1,y1,x2,y2))