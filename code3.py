"""
write a script that will ask user on the street to enter yes or no as answer.
if the user anser is not either yes or no,the script should keep asking for a valid entry.
and if the entry is yes or no, then it should display valid entry
"""
user_answer=""
while True:
    if user_answer not in ['yes','no']:
        user_answer=input("Do you want a covid shot? please enter (yes or no):  ").lower()
    else:
        print("valid choice")
        break    