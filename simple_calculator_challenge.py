# -------------------------------------------- 

	# You've just learned all about functions. 
	# Now take what you've learned to create your own

					# CALCULATOR!

	# We'll guide you through the first few steps,
	# then you'll have a chance to add your own features
	# that will make this your new go-to calculator!

  # -------------------------------------------- 

print("My Simple Calculator")

# -------------------------------------------- 

# Part 1: 

	# The first features of any simple calculator is that
	# it should be able to perform the basic math operations. 
	# Let's start by writing the functions we'll need to execute 
	# the following operations:

		# Addition
		# Subtraction

# -------------------------------------------- 

# Sum

def add_numbers(num1, num2): 
	return num1 + num2

sum = add_numbers(5, 6)
print(sum)
#_____________________________________________________________

# Subraction

def sub_numbers(num1,num2):
	return num1-num2

print(sub_numbers(5,6))

#_____________________________________________________________

# Multiplication

def multiply_numbers(num1, num2):
	return num1 * num2

print(multiply_numbers(4,4))
#_____________________________________________________________

# Division

def divide_numbers(a,b):
	answer = a/b
	return answer

print(divide_numbers (4,4))

# ____________________________________________________________

# Part 3: 

	# Now that you have your basic functions in place, you need to get some user input.
	# What's a calculator for if no one is using it?

# Write a function that will prompt the user for the operation they want to call and the values they are inputting.

# -------------------------------------------- 
print("The Simple Calculator")

print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")

print(input("Choose which math you want to use "))

user_number = input("type a #")












# -------------------------------------------- 

# Part 4: 

	# Now that you have all of the basic four operations completed, you get to add your own features!
	# What will you add to make this your go-to calculator? 

	# Stuck? : Think about what you count/calculate on a (almost) daily basis.
	# Can you write a function that will take in the data you need and do the calculation for you? 

	# (I know I calculate how many hours of sleep I get every day... ｡(*^▽^*)ゞ )

# -------------------------------------------- 

# Write a function or functions that will add some unique features to your calculator. 
# Don't forget to:
		# Give your function an name and parameters that are self explanatory and written in camelcase!
		# Use comments throughout your code
		# Test your code!
  
# -------------------------------------------- 





















# -------------------------------------------- 
# Ignore this section. This is just for checking your work

def check_answers(gen_answer, correct_answer):
    if gen_answer == correct_answer:
        print("Your code works!")
    else:
	    print(f"Try again, your code generated {gen_answer} but the correct answer is {correct_answer}")