#********************************************************************
 #                                                                  
 #  Team Edge List Mini-project: FOR LOOP CHALLENGES
 # 
 #   Complete the following loop challenges below. Follow the ToDos
 #   1. COUNTER: Write a loop that prints a happy birthday message for every
 #      year you have been alive.
 #   2. ITERATOR: Write a for for loop that prints every item in a list

 #   3. EVEN COUNTDOWN: Write a for loop that counts down from 100 to 0, 
 #      printing only the odd numers
 #   4. FINDER: Write a function that takes in a list and a word and prints 
 #      CONGRATULATIONS!! if the word is found in the list
 #   5. NESTED: Write a function that logs every letter in a sentence
 # 
 # ***************************************************************/
import random

print("------------------- CHALLENGE 1 : COUNTER -------------------")

#this list prints every number between 0 and 10, using range

for x in range(11):
    print("Counter at: " + str(x))
   

#-->TODO: Write a loop that prints a happy birthday message for every year you have been alive.

for y in range(17):
    print(f"Happy Birthday Mario!!!! Today you are {y} years old")

print("------------------- CHALLENGE 2 : ITERATOR ----------------------")

#here is a list full of colors...
colors = ['red' , 'violet' , 'cyan' , 'pink' , 'lime' , 'white' , 'yellow', 'black' , 'magenta', 'green', 'orange']

#This is how you can iterate through a list:
for x in colors:
    print("The color is: " + x)

#-->TODO: Declare a list with at least 5 animals. You provide the animals.
animals = ['Hamsters', 'Hedgehogs', 'Elephants', 'Camelones', 'Lions']

#-->TODO: Print all the animals in the array with a for loop. 

for x in animals:
    print(f"An animal that I want are {x}")

print("------------------- CHALLENGE 3 : EVEN COUNTDOWN ------------------")


#The line below makes a random number between 0-50 and assigns it to the random variable
random = random.randint(0, 50)

#this if/else statement checks if the number is even using the modulo operator (%)
if random % 2 == 0:
    print(str(random) + " is even!")
else:
    print(str(random) + " is odd!")

#-->TODO: Write a function that counts BACKWARDS from 100 and prints only even numbers

def backward_counter():
    for x in range(100,0,-2):
        print(x)

backward_counter()

#-->TODO: Write a function that counts BACKWARDS from the given random number and prints only odd numbers
new_list = []

def backward_counter1():
    for x in range(100,0, -2):
        if(x % 2 != 0):
            new_list.append(x)
        print(x)

backward_counter1()

print("------------------- CHALLENGE 4 : Finder ------------------")

#This code uses the in operator to see if an element exists in a list. It only has to appear once.
color = input('Type a one word color and see if it is one of my favorite colors! >> ')
if color in colors:
    print("Yes, that color is a fav")
else:
    print("No, that color is not one of my favorites")

#-->TODO Declare a list of any strings you  want: cities, friends, movies, etc.

strings = ['Oakland']

#-->TODO Write function to prompt the user to "Guess" if an element is present in your list. Store their response in a variable. 
#   --> If their guess is in your list, print CONGRATULATIONS!


#-->TODO Call your function.



print("------------------- CHALLENGE 5 : Nested ------------------")

#this is how you get the length of a word:
big_word = "antidisestablishmentarianism"
print(f"{big_word} has {len(big_word)} letters")

#this is how you can nest for loops, one inside the other! These loop through all the colors, and then through all the characters in the color
for color in colors:
#for all the colors:
    print(color)
    for c in color:
        print(" - " + c) #log each letter. Remember, a string is also an array of characters.


#-->TODO Write a function that prints every letter in a sentence that a user enters.

user_input = input("What word do you want to put in?: ")
# print(f"{user_input} has {len(user_input)} letters")

for i in user_input:
    print(i)

#-->CHALLENGE: Let the user know which word is the shortest one!
