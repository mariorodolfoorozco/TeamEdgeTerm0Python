import random

import time
from random import randint
teller = dict([
            (1,"Ask again later."),
            (2,"Better not tell you now."),
            (3,"Cannot predict now"),
            (4,"Most likely"),
            (5,"As I see it, yes"),
            (6,"It is decidedly so"),
            (7,"Yes definitely"),
            (8,"You may rely on it"),
            (9,"Without a doubt"),
            (10,"It is certain"),
            (11,"Yes"),
            (12,"Signs point to yes"),
            (13,"No."),
            (14,"Don’t count on it"),
            (15,"Outlook not so good"),
            (16,"My sources say no"),
            (17,"Very doubtful"),
            (18,"Sucks to suck ¯\_(ツ)_/¯"),
            (19,"Lmao no"),
            (20,"Not at all, you utter buffoon."),
            (21,"Cannot predict now"),
            (22,"Reply hazy try again"),
            (23,"My reply is no"),
            (24,"Yikes! I don't think you would like the answer. One word: Xanax")
])
question = input("Enter a question: ")

colors = ["BLUE", "GREEN", "ORANGE", "RED"]
num_list_1 = [1,2,5,6]
num_list_2 = [3,8,4,7]

print(colors)
pick_colors = input("Pick a color: ")

temp = ""
temp_arr = []

for i in colors:
  if pick_colors.upper() == i:
    temp = i
    break
for i in range(0, len(temp)):
  if(i % 2 ==0):
    print(f"{temp[i]}\n{num_list_1}")
    temp_arr = num_list_1
  else:
    print(f"{temp[i]}\n{num_list_2}")
    temp_arr = num_list_2
  time.sleep(1)
pick_num =None
while pick_num not in temp_arr:
  pick_num = input("Pick a number below the last letter of your color: ")
  pick_num = int(pick_num)
  if pick_num not in temp_arr:
    print("Please pick the numbers below the last letter")
    time.sleep(1)

temp_arr_1 = []
for i in range(1,int(pick_num)+1):
  if i % 2 == 0:
    print(f"{i}\n{str(num_list_2)}")
    temp_arr_1 = num_list_2
  else:
    print(f"{i}\n{str(num_list_1)}")
    temp_arr_1 = num_list_1
  time.sleep(1)
choice = None
while choice not in temp_arr_1:
  print("Pick a number from your list")
  choice = int(input())

choice = choice * randint(1,3)
print(teller[choice])

 
