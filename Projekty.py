# 1. Band name generator:

print("Welcome to your Band Generator program!")
city = input("What is the name of the city you grew up in?\n")
pet = input("What is the name of your pet?\n")
print("The name of your band could be:", city + " " + pet)

# 2. Type a two digit number and I will add the digits for you:

two_digit_number = input("Type a two digit number and I will add the digits for you: ")
first_digit = int(two_digit_number[0]) 
second_digit = int(two_digit_number[1])
two_digits = first_digit + second_digit
print(two_digits)

# 3. Your BMI Calculator:

print("Your BMI calculator")
height = input('Enter your height here in m: ')
weight = input('Enter your weight here in kg: ')
bmi = float(weight) / float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)

# 4. Life in weeks calculator basing on that you will live 90 years:

print("Life in weeks calculator basing on that you will live 90 years")
age = input("What is your current age? ")
age_num = int(age)
year1_days = (90 * 365) - (365 * age_num)
year1_weeks = (90 * 52) - (52 * age_num)
year1_months = (90 * 12) - (12 * age_num)
print(f"You have {year1_days} days, {year1_weeks} weeks, {year1_months} months left")

# 4. albo inny sposób:

print("Life in weeks calculator basing on that you will live 90 years")
age = input("What is your current age? ")
age_int = int(age)
years_remaining = 90 - age_int
days_remaining = 365 * years_remaining
weeks_remaining = 52 * years_remaining
months_remaining = 12 * years_remaining
message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left"
print(message)

# 5. Welcome to the Tip calculator:

print("Welcome to the Tip calculator.")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")
total_bill_float = float(total_bill)
tip_percentage_float = float(tip_percentage)
num_people_float = float(num_people)
tip_amount = (tip_percentage_float / 100) * total_bill_float
bill_amount = round((tip_amount + total_bill_float) / num_people_float, 2)
final_bill_amount = "{:.2f}".format(bill_amount)
message = f"Each person should pay: ${final_bill_amount}"
print(message)

# 6. Type up a number to check if it is odd or even:

print("Type up a number to check if it is odd or even:")
num = int(input("Please put your number in here: "))
if (num % 2 == 0):
            print(f"Number {num} is a even number")
else:
            print(f"Number {num} is an odd number")

# 7. Rollercoaster entry calculator:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster :)")
  age = int(input("What is your age? "))
  if age >= 18:
    print(f"Your age is {age}, please pay 12 zł.")
  elif age >= 12:
    print(f"Your age is {age}, please pay 7 zł.")
  else:
    print(f"Your age is {age}, please pay 5 zł." )
else: 
  print(f"Sorry, your height is {height} cm, you have to grow taller before you can ride :(")

# 7.1. Rollercoaster entry calculator + photo taken:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster :)")
  age = int(input("What is your age? "))
  if age > 18:
    bill = 12
    print(f"Your age is {age}, you are an adult, please pay 12 zł." )
  elif age > 12:
    bill = 7
    print(f"Your age is {age}, you are a youth, please pay 7 zł.")
  else:
    bill = 5
    print(f"Your age is {age}, you are a child, please pay 5 zł.")
  wants_photo = input("Would you like a photo to be taken? Please put Y or N: ")
  if wants_photo == "Y":
    bill += 3
 
  print(f"Your final bill is {bill} zł.")
else:
  print(f"Sorry, your height is {height} cm, you have to grow taller before you can ride :(")

# 7.2. Rollercoaster entry calculator + photo taken + middle age crisis discount:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster :)")
  age = int(input("What is your age? "))
  if age < 12:
    bill += 5
    print(f"Your age is {age}, you are a child, please pay 5 zł." )
  elif age < 18:
    bill += 7
    print(f"Your age is {age}, you are a youth, please pay 7 zł.")
  elif age >= 45 and age <= 55:
    print(f"Congratulations, your age is {age}, you get a middle age crisis discount and you get your entry for free :)")
  else:
    bill += 12
    print(f"Your age is {age}, you are an adult, please pay 12 zł.")
  wants_photo = input("Would you like a photo to be taken? Please put Y or N: ")
  if wants_photo == "Y":
    bill += 3
  print(f"Your final bill is {bill} zł.")
else:
  print(f"Sorry, your height is {height} cm, you have to grow taller before you can ride :(")
  
# 8. BMI Calculator 2 - containing BMI's descriptions (nested loops used):

print("Welcome to your BMI calculator.")
height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / (height ** 2 / 10000))
if bmi >= 35:
  print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi >=  30:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 25:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 18.5:
  print(f"Your BMI is {bmi}, you have a normal weight.")
else:
  print(f"Your BMI is {bmi}, you are underweight.")

# 9. Check for Leap year:

print("Check for a Leap year")
your_year = int(input("Please type up a year you would like to check for a Leap year here: " ))
leap_year = your_year % 4 == 0 and (your_year % 100 != 0 or your_year % 400 == 0)
if leap_year:
  print(f"Year {your_year} is a Leap year.")
else:
  print(f"Year {your_year} is not a Leap year.")

# 9.1. Check for Leap year (another way):

print("Check for a Leap year")
your_year = int(input("Please type up a year you would like to check for a Leap year here: " ))
if your_year % 4 == 0:
  if your_year % 100 == 0:
    if your_year % 400 == 0:
      print(f"Year {your_year} is a Leap year.")
    else:
      print(f"Year {your_year} is not a Leap year.")
  else:
    print(f"Year {your_year} is a Leap year.")
else:
  print(f"Year {your_year} is not a Leap year.")

# 10. Pizza order practice:

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
  bill = 15 
if size == "M":
  bill = 20
if size == "L":
  bill = 25
if add_pepperoni == "Y":
  bill += 3
if extra_cheese == "Y":
  bill += 1
print(f"Your final bill is ${bill}.")

# 10.1. Pizza order practice other way:

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
if extra_cheese == "Y":
  bill += 1
print(f"Your final bill is ${bill}.")

# 11. Love Calculator project:

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")

# 12. Treasure Island game:

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("Before you decide if you want to try your luck finding the treasure, please be aware that the adventure will be very dangerous, so think twice, before you make the decision, because after you start, there won't be a way back.")
decision = input("Please let me know what is your decision by typing up Y or N: ")

if decision == "Y" or decision == "y":
  print('''You are very brave! Now you will get a chance to find one of the most wanted treasures in the world, Captain's Blackbeard treasure. Now you get on a private jet and you will be dropped over your destination. However, after you get to the place, you will still have to make your way through to the treasure. Be aware that many tried before, but so far now one has made it! Be the first one!
        _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\ ''')
  first_choice = input("You were dropped on a desert island, somwhere in the pacific ocean. You landed in between 2 massive rock mountains. Now there are only 2 ways forward. Which one will you take? Left or right: ")
  if first_choice == "Left" or first_choice == "left":
    print('''After a long walk you get to a massive river.                 _.._
   _________....-~    ~-.______
~~~                            ~~~~-----...___________..--------
                                           |   |     |
                                           | |   |  ||
                                           |  |  |   |
                                           |'. .' .`.|
___________________________________________|0oOO0oO0o|____________
 -          -         -       -      -    / '  '. ` ` \    -    -
      --                  --       --   /    '  . `   ` \    --
---            ---          ---       /  '                \ ---
     ----               ----        /       ' ' .    ` `    \  ----
-----         -----         ----- /   '   '        `      `   \
     .-~~-.          ------     /          '    . `     `    `  \
    (_^..^_)-------           /  '    '      '      `
                    --------/     '     '   ' " ''')
    second_choice = input("Now you look on the map and you know that this is the right path, and to follow it, you need to cross the river. You can either cross it, or wait until you build a raft to get on the other side. What do you do? swim or wait: ")
    if second_choice == "wait" or second_choice == "Wait":
      print('''Well done! You managed to build a raft and you got on the other side. You carry on walking following your map. You get to a huge pyramid. You found the place!
    
                 /\.
                /|_\`.
               /__|_\/`.
              /__|__|\/.`.
             /_|__|__|\/`/`.
            /|__|___|__\/`/
           /__|___|___|_\/ ''')
    
      third_choice = input("You can see 3 doors now and you have to choose which one will you go through to get inside. Which one will you choose? Red, blue, or yellow: ")
      if third_choice == "Yellow" or third_choice == "yellow":
        print('''Congratulations! You found a treasure and you become extremely rich and famous :) *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
******************************************************************************* ''')
      elif third_choice == "red" or third_choice == "Red":
        print('''Unfortunately you made a wrong choice, you get into room full of fire and you get burned in fire :( Game over.  (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' ) ''')
      else:
        print('''You fell into a whole, ending up in a river and got eaten by a huge fish :( Game over.                  ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\ ''')
  
    else:
      print('''When swimming in the river you got eaten by a huge, angry fish :( Game over.                  ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\ ''')
  else:
      print('''You fell into a whole, ending up in a river and got eaten by a huge fish :( Game over.                  ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\ ''')
  
  
    
  
elif decision == "N" or decision == "n":
  print("Maybe you are not the most brave person in the world, but at least you will stay safe :)")
else:
  print("Please make the correct choice!")

# 13. Heads and Tails project:

import random

random_side = random.randint(0, 1)
if random_side == 0:
  print("Heads")
else:
  print("Tails")
  
# 14. Banker Roulette project:

print("Welcome to Banker Roulette!")
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
from random import randrange
random_name = randrange(len(names))
print(f"{names[random_name]} is going to buy a meal today!")


