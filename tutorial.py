# number = 22
# health = 100

# print(f"{number} {health}")

# def square(x):
#     ans = x * x
#     return ans

# solution = square(6)
# print(solution)

# def toCelsius(f):
#     c = round((+f - 32) * 5/9, 1)
#     print(f"the value in farenheit {f} while the value in celsius {c}")

# toCelsius(33)


# def get_punched(health, armor=0):
#     punch = 50 - armor
#     damage_after_punch = health - punch
#     return damage_after_punch

# def get_slashed(health, armor=0):
#     slash = 100 - armor
#     damage_after_slash = health - slash
#     return damage_after_slash


# def test(health, armor):
#     print(f"Health: {health}, Armor: {armor}")
#     print(f"Health after punch: {get_punched(health, armor)}")
#     print("=====================================")
#     print(f"Health: {health}, Armor: {armor}")
#     print(f"Health after slash: {get_slashed(health, armor)}\n")
#     print("=====================================")
#     print(f"Health: {health}, Armor: no armor!")
#     print(f"Health after slash: {get_slashed(health)}\n")
#     print("=====================================")
#     print(f"Health: {health}, Armor: no armor!")
#     print(f"Health after punch: {get_punched(health)}")
#     print("=====================================")


# test(400, 5)
# test(300, 3)
# test(200, 1)


# def swordSlash(health, armor= 0):
#     slash = 50 - armor
#     healthAfterSlash= health - slash
#     return healthAfterSlash

# print(f"your health is {swordSlash(100)}")
    
# def get_title(first_name, last_name, job):
#     title = first_name + " " + last_name + " the " + job
#     return title


# # Don't touch below this line


# def test(first_name, last_name, job):
#     title = get_title(first_name, last_name, job)
#     print(f"First name: {first_name}")
#     print(f"Last name: {last_name}")
#     print(f"Job: {job}")
#     print(f"Title: {title}")
#     print("=====================================")


# test("Frodo", "Baggins", "warrior")
# test("Bilbo", "Baggins", "thief")
# test("Gandalf", "The Grey", "wizard")
# test("Aragon", "Son of Arathorn", "ranger")

# number = int(input('how old are you'))

# def age(age):
#     year = 2024 - age
#     return year

# print(f"you were born on {age(number)}")

# creditScore = int(input('what is your credit score?'))
# income = int(input('what is your income'))

# def loan(credit, income):
#     if credit > 200 and income > 500000:
#         print('youre approved')
#     elif credit < 200:
#         print ('your credit is too low')
#     elif income < 500000:
#         print ('your income is too low')
#     else:
#         print('you cant be approved for the loan')

# print(loan(creditScore, income))

# i = 1

# while i <= 5:
#     print("*" * i)
#     i = i + 1
# print('done')

# number = 9
# guesses = 0
# guessCount = 3

# guessing game
# ----------------------------------------------------------------

# while guesses < guessCount:
#     guess = int(input("guess the number"))
#     guesses = guesses + 1
#     if guess == number:
#         print(f'congrats the number is {number}')
#         break
# else:
#     print('womp womp')


# car game
# --------------------------------

# action = input('what do you want to with your car').lower()
# started = False

# while True:
#     if action == 'start':
#         if started == False:
#             action = input('your car is running what are you doing now').lower()
#             started = True
#         elif started == True:
#             action = input('your car has already been started')
#     elif action == 'stop':
#         if started == True:
#             action = input('your car has stopped what are you doing now').lower()
#             started = False
#         elif started == False:
#             action = input('your car is no longer running')
#     elif action == 'quit':
#         break
#     else:
#         print('i dont understand')
#         action = input('please input start, stop or quit').lower()
# print("Goodbye!")

# for loop
# ----------------------------------------------------------------
# character =  input('what would you like to iterate')

# def iterate(subject):
#     for i in subject:
#         print(i)

# iterate(character)


# for in range
# ----------------------------------------------------------------
# for i in range(5,20):
#     print(i)

# price calculator
# ----------------------------------------------------------------
# prices =[10,20,30,40,50,60,70,80,90,100]
# total = 0

# for i in prices:
#     total += i
#     print(total)

# print(total)


# nested loops
# ----------------------------------------------------------------

# for i in range(4):
#     for j in range(4):
#         for k in range(4):
#             print(i, j, k)


# x shape with nested loops
# ----------------------------------------------------------------

# array = [5, 2, 5, 2, 2]

# for i in array:
#     print("*" * i)

# for i in array:
#     output = ''
#     for count in range(i):
#         output += 'x'
#     print(output)


# finding the largest number in an array
# ----------------------------------------------------------------

# numbers =[20, 30, 10, 5, 50, 100, 20]
# print(type(numbers))
# max = 0

# for i in numbers:
#     if i > max:
#         max = i
# print(max)


# iterating over nested arrays
# ----------------------------------------------------------------

# array = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [12,13,14,15, 16]
# ]

# for i in array:
#     for j in i:
#         print(j)


# remove duplicates
# ----------------------------------------------------------------
# numbers =[20, 30, 10, 5, 50, 100, 10, 20, 20, 10]
# numbers.sort()
# uniques = []

# for i in numbers:
#     if i not in uniques:
#         uniques.append(i)
# print(uniques)


# unpacking = destructuring in python
#----------------------------------------------------------------
# numbers =[20, 30, 10]
# x,y,z= numbers

# print(x)

# Dictionaries
# ----------------------------------------------------------------
# users = {'username':'john Doe', 'password':'12345678', 'first_name':'John', 'last_name':'Doe'}

# print(users.get('username'))

# number converter
# ----------------------------------------------------------------
# phone = input('Enter phone number')

# numbers = {
#     "1": "one", "2": "two", "3": "three", "4": "four",
#     "5": "five", "6": "six", "7": "seven", "8": "eight",
#     "9": "nine", "0": "zero"
# }

# output =''

# for i in phone:
#     output += numbers.get(i,'!') + ' '
# print(output)


# emoji converter
# ----------------------------------------------------------------

# message = input('>')
# word = message.split(' ')

# output =''

# emojis ={
#             ":)":"(❁´◡`❁)", 
#             ":(":"😩"
#         }

# for i in word:
#     output += emojis.get(i, i) + ' '
# print(output)


# classes
# ----------------------------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print('move')

#     def draw(self):
#         print('draw')


# point = Point(10,20)
# print(point.x)
# point.draw()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f'hello {self.name}')


# me = Person('daniel')
# print(me.name)
# me.talk()


# inheritance
# ----------------------------------------------------------------


# class Mammal:
#     def __init__(self, name):
#         self.name = name
    
#     def walk(self):
#         print(f'walking {self.name}')

# class Dog(Mammal):
#     pass

# class Cat(Mammal):
#     def purr(self):
#         print(f' {self.name} is purring')


# lucy = Dog('lucy')
# lucy.walk()

# james = Cat('james')
# james.purr()