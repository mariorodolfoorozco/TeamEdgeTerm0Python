#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/

active = True

print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n"

print(welcome_message)


#-->Todo: declare a shopping_list list


shopping_list = ["Dragon Fruit", "Milk", "Eggs", "Medicine", "Avocado"]
print("This is your shopping list " + str(shopping_list))

def prompt_user():

    reply = input("What do you want to add or remove?  >>  ")

    return input("Anything else?  >>  ")

def check_answer(ans):
    if ans in shopping_list:
        remove_item(ans)
        print(shopping_list)
    else:
        add_item(ans)
        print(shopping_list)


def add_item(ans):
    shopping_list.append(ans)


def remove_item(ans):
    shopping_list.remove(ans)

while active:

    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True
