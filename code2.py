#question1 : Write a code that will take a string from user , and display how many characters are in that string
"""
year=input("how long have you been in it industry?")
print("your number of year is: ", year)
#then len
my_string="you deserve a long vacation"
print(len(my_string))
"""
#question2 : Write a code that will take a string from user and if the string has less than 4 charactars, it should display "invalid entry" and 
    	# if the characters number in the string is more that 4 , it should display "valid entry"
"""
your_password=input("what is your pass word?")
if len(your_password) > 4 :
    print("Invalid entry")

elif len(your_password) < 4:
    print("Valid entry")
"""
#question3 :  Write a code that will take email address as input and check if @ is in the email receive to tell the user if the email is valid or not.    
"""
email_address=input("enter your email address")

if '@' in email_address:
        print(f"{email_address} is a valid email address.")
else:
        print(f"{email_address} is not a valid email address.")
"""        
#question4 :  Username and password of an application is admin. Write a code that takes two inputs from user username and password and tell the user 
    	 # "wrong username or password" if the username and password entered is not admin; and if it is admin and admin, it display "successfully login"
"""
your_username = input("Enter username: ")
your_password = input("Enter password: ")
if your_username == "admin" and your_password == "admin":
        print("Successfully logged in!")
else:
        print("Wrong username or password.")
"""
#question5 : Write a program to take users zip code and check if the input data was a digit number with 5 digits. 
     # 	(a good zip code has 5 digits) if it is good , display "your entry is valid" if not , display "please enter a valid entry"
"""
zip_code = input("Enter your zip code: ")

if zip_code.isdigit() and len(zip_code) == 5:
        print("Your entry is valid.")
else:
        print("Please enter a valid entry.")
"""

#question6 : Write a script that will take two integers and give the sum of those two int. 
"""
num1 = float(input("Enter the first integer: "))
num2 = float(input("Enter the second integer: "))
sum = num1 + num2
print("sum:",sum)
"""

#question7: Write a script that will take two integers and give the sum of those two int.
""" 
int1= float(input("enter number1: "))
int2= float(input("enter number2: "))
total_sum = int1 + int2
print("total_sum:", total_sum) """

#question8:  write a script that will take user's age and tell if there are eligible to vote or not. 

age=float(input("enter your age: "))
if age >= 18:
   print("you are eligible to vote.congratulation !!! ")
else:
    print("you are not eligible to vote.")