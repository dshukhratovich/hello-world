# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# See PyCharm help at https://www.jetbrains.com/help


for x in range(0, 20):
    if x % 5 > 3:
        print(x)
        # COMPLETE PYTHON BOOTCAMP GO FROM ZERO TO HERO IN PYTHON 3
        # 00 Python Object and Data Structure Basics

        # Numbers
a = 3.345
print(type(a))
x = 9.43477796
pi = x / 3
print(pi)
print(16 ** 0.5)
# Lists & Strings
a = ["hdk", "ueshr", "389", "uj6"]
print(a[-1])
print("this \tis \talso \ta \tstring")
print("this \nis \nalso \na \nstring")
print(len("xjhfvxfkvnzl34895fhvzf"))
print(len(a))
b = "My Name Is Dadakhon"
print(b[5:-5])
print(b[::3])
print(b[1:-1:4])
print(b[::-1])
m = "Dadakhon"
h = "Shukhratovich"
k = h[0:-5]
heb = "ajrgv aeorigv aeiorveave54 w488 7"
print(heb.split(sep="a"))
print(heb.split(maxsplit=0))
name1 = "Khudoyberganov " + k
name2 = m + " " + h
print(name1.lower())
print(name2.upper())
p = "I like watching porn at home"
print(p.split())
print("I like watching porn {} at home".format(" in 4K"))
o = "in HD"
print(f"I like watching porn {o} at home")
a.append("cdddec")
a.pop(0)
a.sort()
a.insert(2, "dkf")
a.insert(3, "cdddec")
print(a.count("cdddec"))
print(a)
a.reverse()
print(a)
# Dictionaries
my_dict = {'RedmiNote8': '199$', 'OnePlus8': '699'}
print(my_dict['RedmiNote8'])
r = {"k1": ['1', '3', 'f', 'uEHF'], "k2": {'inside': [1, 0]}}
my_dict['iPhone12mini'] = "599$"
print(r["k1"][3])
print(r["k2"]["inside"][0])
print(my_dict)
print(my_dict.keys())
# Tuples
t = (1, "fkj", 345, 143,235,235,"safd")
tupea = t.index(1)
# cannot reassign objects in tuples unlike lists
# Sets
my_set = [2, 4, 5, 5, 6, 4, 2, 2, 4, 5, 2]
print(my_set)
print(set(my_set))
# IO Files
# myfile = open('myfile.txt')
# print(myfile.read())
# myfile.seek(0)
# print(myfile.read())
# secondfile = open('C:\\Users\\shukhratovich\\Documents\\2ndfile.txt')
# with open('C:\\Users\\shukhratovich\\Documents\\2ndfile.txt', mode='a') as p:
#      p.write('a')
# print(secondfile.close())
# print(open('C:\\Users\\shukhratovich\\Documents\\2ndfile.txt').read())
# with open('skhfb', mode='w') as n:
#     n.write("My first file that I created on Python")
# print(open('skhfb').read())
# Assestment Test
op = [23, 34, 'w35', [23, 'hello']]
op[3][1] = 'goodbye'
print(op)
oa = [123, 236, 26, 4]
oa.sort()
print(oa)
d = {'simple_key': 'hello'}  # easy
print(d['simple_key'])
d = {'k1': {'k2': 'hello'}}  # a little tricky
print(d['k1']['k2'])
d = {'k1': [{'nestkey': ['this is deep', ['hello']]}]}  # more trikier
print(d['k1'][0]['nestkey'][1][0])
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}  # hard and annoying
print(d['k1'][2]['k2'][1]['tough'][2][0])
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
print(l_one[2][0] >= l_two[2]['k1'])
# 01 Comparison Operators
print(3 != 4)
# 02 Python Statements
dog_is_hungry = False
if dog_is_hungry:
    print("FEED_ME!")
else:
    print("I'M_NOT_HUNGRY")

location = "Whole Foods"
if location == 'Bank':
    print('I have a lot of money')
elif location == 'Apple Store':
    print("iPhone's are expensive")
else:
    print(f"I didn't go to the {location} today")

for x in range(1, 10):
    if x % 2 == 0:
        print(f"{x} is an even number")
    else:
        print(f"{x} is an odd number")
y = 0
for x in range(100):
    y = y + x
print(y)

p = 1
for x in range(1, 6):
    p = p * x
print(p)  # if i don't include print(p) in the for statement i only get the intentional result

my_list = [(1, 2), (4, 7), (9, 4)]
for x in my_list:
    print(x)
for x, y in my_list:  # feature of the Tuples
    print(x, y)

d = {'k1': 1, 'k2': 2, 'k3': 3}
for x in d:  # for values, use d.values() instead of d
    print(x)
for x, y in d.items():  # feature of the Dictionaries
    print(x, y)

x = 1
while x < 10:
    x += 2  # use 'pass' to do nothing
    print(x)
for x in range(5):
    if x == 3:
        continue
    print(x)
for x in range(5):
    if x == 3:
        break
    print(x)
# range operator --> range(start,stop,step),  list(range(...)) makes list of integers in the given range
x = 'shukhratovich'
for z, y in enumerate(x):  # --> enumerate operator
    print(z, y)

for x, y in zip('khdnc', range(4)):  # --> zip operator
    print(x, y)

# in operator --> check if a particular 'key,value,object' is in the 'list,dictionary,set,string,tuple'
d = {'key1': 34, 'key2': 65}
print(34 in d.values())
print('key2' in d.keys())

# min and max operators --> identifies minimum and maximum values in a list
l = [36, 25, 6795, 235, 25, 2, 7]


class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,deposit):
        self.balance += deposit
        return f"Your ${deposit} Deposit Accepted!"

    def withdraw(self,withdraw):
        if self.balance > withdraw:
            self.balance -= withdraw
            return f"You have withdrawed ${withdraw} succesfully!"
        else:
            return "You don't have enough '$$$' funds available."
print(min(l))
print(max(l))

# random operator --> selects a random object from a list
from random import randint

print(randint(0, 100))
list2 = list(range(10))
from random import shuffle

shuffle(list2)
print(list2)
firstnum = randint(0, 100)
secondnum = randint(0, 100)
print(firstnum + secondnum)


# result = input('Enter a number:')      #to make the reuslt number use int or float function
# print(int(result) + randint(0,10))


mystr = 'iausfn'  # method1
list3 = []
for x in mystr:
    list3.append(x)
print(list3)

# method2

list5 = [x ** 2 for x in range(10)]
y = 0
for x in list5:
    y = y + x
print(y)
list6 = [x ** 3 for x in range(5) if x % 2 == 0]
print(list6)
list7 = [15, 32, 40, 25, 30]
fahrenheit = [((9 / 5) * temp + 32) for temp in list7]

print(fahrenheit)
list8 = []
for x in range(1, 4):
    for y in range(4, 7):
        list8.append(x * y)
print(list8)
list9 = [x * y for x in range(1, 4) for y in range(4, 7)]

print(list9)
# Assestment Test 2
ps = "Sam Print out only the words that Starts with S in the Sentence"

for x in ps.split():
    if x[0].lower() == 's':
        print(x)
listx = [x for x in range(1, 51) if x % 3 == 0]

print(listx)
st = 'Print every word in this sentence that has even number of letters'

for x in st.split():
    if len(x) % 2 == 0:
        print('even!')

for x in range(1, 101):
    if x % 15 == 0:
        print('FizzBuzz!!')
    elif x % 3 == 0:
        print('Fizz!')
    elif x % 5 == 0:
        print('Buzz!')
    else:
        print(x)
st1 = 'Create a list of the first letters of every word in this string'

for x in st1.split():
    print(x[0])
list2 = [x[0] for x in st1.split()]

print(list2)
str1 = '76542'

print(str1[::-1])
lisssst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(lisssst[1::2])

for x in range(7):
    print(x ** 3)
s = 1
sum = 0

for i in range(0, 2):
    print(s, end='')
    sum += s
    s = (s * 10) + 1
    print(sum)

def function_1(x='unknown individual'):
    return 'hello ' + x

def dog_check(mystr):
    return 'dog' in mystr.lower()
print(dog_check(mystr='yes Dog is in the string'))

def myfunc(*args):
    return sum * 0.29
print(myfunc(3, 545.457, 7, 246, 75))

def myfunc1(**kwargs):
    if 'fruit' in kwargs:
        print(f'my fruit choice is {kwargs["fruit"]}')
    else:
        print("I didn't find any fruit here")
print(myfunc1(fruit='apple'))

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)

def animal_crackers(text):
    a = text.lower().split()
    return a[0][0] == a[1][0]

def makes_twenty(a, b):
    return a == 20 or b == 20 or a + b == 20

def old_macdonald(name):
    g = name[:3]
    b = name[3:]
    return g.capitalize() + b.capitalize()  # i can also use upper() method

def list_to_string(string):
    str1 = " "
    return str1.join(string)

def master_yoda(sentence):
    a = sentence.split()
    return list_to_string(a[::-1])
# return abs(100-n)<=10 or abs(200-n)<=10    #absolute value --> {sonning moduli(o'zbekcha)}

def almost_there(n):
    return 90 <= n <= 110 or 190 <= n <= 210

def has_identical(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

def paper_doll(text):
    result = ""
    for i in text:
        result += i * 3
    return result


def summer_69(arr):

    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print("this is a test")


def list_to_string(list):
    str1 = " "
    return str1.join((list))
print('This is a Test')
t = (1, 4, 67)
tlist = list(t)


print(tlist)


def spy_game(nums):
    code = [0, 0, 7, 'i']

    for i in nums:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([0, 8, 0, 7]))


def count_primes(num):
    primes = [2, 3, 5, 7]
    for i in range(2,num + 1):
        for x in range(2, 10):
            if i % x == 0:
                break
        else:
            primes.append(i)
    return primes
print(count_primes(19))


print(list_to_string(['asf', 'ef']))


def cube(nums):
    return nums ** 3
nums = [2, 4, 3, 1]

for item in map(cube, nums):
    print(item)


print(list(map(cube, nums)))


def splicer(strings):
    if len(strings) % 2 == 0:
        return 'Even'
    else:
        return strings[0]
a = ['Andy', 'Eve', 'Sally']


print(list(map(splicer, a)))


def check_3(num):
    return num % 3 == 0
listnums = [4, 6789, 34, 63, 99]

print(list(filter(check_3, listnums)))  # filter works only in booleans

for n in filter(check_3, listnums):
    print(n)
square = lambda num: num ** 2
print(square(16))
list1 = list(map(lambda n: n ** 4, nums))
print(list1)
print(list(filter(lambda n: n % 3 == 0, list1)))
print(list(map(lambda i: i[::-1], a)))


# rad = int(input('Enter the Radius of the Sphere: '))

pi = 3.14159265


def volume_sphere(rad):
    return (4 / 3) * pi * (rad ** 3)


print(volume_sphere(4))


def ran_check(num, low, high):
    if num in range(low, high + 1):
        return f"{num} is the in range of {low} and {high}"
    else:
        return f"{num} is NOT in the range of {low} and {high}"


print(ran_check(3, 1, 10))


def up_low(mystr):
    d = {'upper': 0, 'lower': 0}
    for w in mystr:
        if w.isupper():
            d['upper'] += 1
        elif w.islower():
            d['lower'] += 1
        else:
            pass
    return f"No. of upper case characters: {d['upper']} \nNo. of lower case characters : {d['lower']}"

print(up_low('Hi, My name is Dadakhon'))


list2 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]


def unique_list(lis):
    return list(set(lis))

print(unique_list(list2))


sample_list = [1, 2, 3, -4]


def multiply(nums):
    total = 1
    for i in nums:
        total = total * i
    return total


print(multiply(sample_list))


def palindrome(string):
    return string[::-1] == string


print(palindrome('madam'))


def is_panagram(str):
    return 'a' and 'b' and 'c' and 'd' and 'e' and 'f' and 'g' and 'h' and 'i' and 'j' and 'k' and 'l' and 'm' and 'n' and 'o' and 'p' and 'q' and 'r' and 's' and 't' and 'u' and 'v' and 'w' and 'x' and 'y' and 'z' in str.lower()
print(is_panagram('The quick brown fox jumps over the lazy dog'))


print(is_panagram('abcdefghijklmnopqrstuvwxyz'))


class Dog():
    specie = "ANIMAL"

    def __init__(self, name, colour, price):
        self.colour = colour
        self.name = name
        self.price = price

    def bark(self, opponent):
        print(f"WOOF! fuck you {self.name} ,fuck you {opponent}")
my_dog = Dog("Mac", "Brown-ish", "2grand")
print(my_dog.specie)


print(my_dog.bark('elikel'))


class Circle():
    pi = 3.14159265

    def __init__(self, radius):
        self.radius = radius
        self.area = Circle.pi * self.radius ** 2
        self.circumference = 2 * Circle.pi * self.radius
my_circle = Circle(3)


print(my_circle.area)

class Triangle(Circle):

    def __init__(self):
        Circle.__init__(self,1)
        print("Inherited")

class Line():

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.distance = ((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2)**0.5
        self.slope = abs((coor1[1]-coor2[1])/(coor1[0]-coor2[0]))

my_line = Line((3,2),(8,10))
print(my_line.distance)

print(my_line.slope)

class Cylinder():
    pi = 3.14159265
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        self.volume = self.height * pi * self.radius**2
        self.surface_area = (2*pi*self.radius * self.height) + 4*pi*(self.radius**2)
my_cylinder = Cylinder(2,3)
print(my_cylinder.volume)

print(my_cylinder.surface_area)

dadakhon_account = Account("Mr.Shukhratovich",10000)
print(dadakhon_account.withdraw(10))
print(dadakhon_account.balance)
print(dadakhon_account.withdraw(563))
print(dadakhon_account.balance)
print(dadakhon_account.deposit(100))
print(dadakhon_account.withdraw(73562))

# strings = "The quick brown fox jumps over the lazy dog"
# name = input('Enter file:')
# handle = open(name)

# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1

# print(counts)

total = 0
for nums in range(1,1000):
    if nums%3==0 or nums%5==0:
        total += nums
print(total)
a = []
for n in range(10):
    a.append(n)
print(a)
fibonacci_l = []
def fibonacci(num):
    a,b = 0,1
    while a<num:
        a, b = b, a+b
        fibonacci_l.append(a)
    return fibonacci_l
    #     else:

total = 0
for n in fibonacci(4000001):
    if n%2==0:
        total+=n

print(total)

print(count_primes(100))
lists = [3,5,4,11,13,20]
mult = []
for i in lists:
    for n in lists:
        if i!=n:
            result = i*n
            mult.append(result)


print(list(set(mult)))
print(len(set(mult)))

def primefactor(n):
    primes = []
    for i in count_primes(n):
        if n%i==0:
            primes.append(i)

    return primes

print(primefactor(145))
pal = 9008

from math import acos
angle = acos(0.5)*57.324840764331206

def angle_cos(n):
    return acos(n)*57.324840764331206

print(f"{angle_cos(0.5):1.0f}°")

from colorama import init
init()
from colorama import Fore
print(Fore.RED + "some red text")
print(Fore.LIGHTRED_EX + "some l_red text")
print(Fore.LIGHTMAGENTA_EX + "some __ text")

from triangle import triangle_specs

print(triangle_specs(6,8,10))

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "I belong to new.py")

try:
    result = 39 + "3"
except:
    print(Fore.RED+"ERROR: LOOKS LIKE YOU'RE FUCKED!!")
else:
    print("Good Job!!")

try:
    f = open("FuckYou.txt",mode='r')
    f.write("Wanna fuck?!")
except TypeError:
    print("You moron, Type Errorrrrrrrrrrrrrrrrrrrrrrrrr")
except IOError:
    print("Oh, Fuck me! IO Errorrrrrrrrrrrrr")
finally:
    print(Fore.RESET+ "I always fuck!")

# while True:
#     try:
#         result = int(input("Plz give me a number:\n"))
#     except:
#         print("Fuck! I'm gonna ask you again.")
#         continue
#     else:
#         print("Hell Yeah!")
#         break

try:
    for i in [a, b, c, d]:
        print(i ** 2)
except:
    print("Whoops! TypeEror.")
try:
    x = 5
    y = 0
    z = x / y
except:
    print("you cannot divide by 0")
finally:
    print("All Done!")


# def squareofit():
#     while True:
#
#         try:
#             n = int(input("Your number:\n"))
#         except:
#             print("An error occured. Plz try again")
#             continue
#         else:
#             return f"Square of your number is {n ** 2}"


# print(squareofit())
from math import pi
from math import radians
nums = [1,3,8,3,4,7,5,3,9]
num = 23.2255225
print(num.__round__(2))
print(180/pi)
print(radians(57.29577951308232))



from random import shuffle


print("Hi Pycharm!")
x = 0
while x<10:
    x+=1
    print(x)

for a in range(1,6):
    for b in range(1,a+1):
        print(b,end='')
    print('')

# x = 0
# result = int(input('Enter any number:'))
# for y in range(1,int(result)):
#     x=x+y
# print(x)
#
# for y in range(1,11):
#     print(result*y)

list1 = [12,4,57,2,5,25,19,20,346,235,65,155,25,4,87,34]
list1.sort()
for x in list1:
    if x>151:
        break
    elif x%5==0:
        print(x)

# print(len(str(result)))
list2=[10,20,30,40,50]
for x in list2:
    list2.reverse()
print(list2)
for i in range(4,-1,-1):
    print(list2[i])

for i in range(-10,0):
    print(i)
print('Done!')

for i in range(25,51):
    for x in range(2,10):
        if i%x==0:
            break
    else:
            print(i)

print('dadakhon',end='_')
print('shukhratovich')
x = 1
# for i in range(1,result+1):
#     if result ==0:
#         print(f"Factorial of {result} is 1")
#     elif result>=1:
#         x = x * i
# print(f"Factorial of {result} is {x}")

def blackjack(a, b, c):
    if a+b+c <= 21:
        return a+b+c
    elif 22 < a+b+c <= 31:
        return "BUST"


print(blackjack(8, 8, 8))


def check_natural_num(a, b, c):
    return a in range(10) and b in range(10) and c in range(10)


print(check_natural_num(9, 4, 1))


def check_prime_num(num):
    '''for numbers in range 143(excluded)'''

    for i in range(2, 10):
        if num % i == 0:
            return f"{num} is not a prime number"
        else:
            return f"{num} is a prime number"


print(check_prime_num(97))



print("This is a Test")



