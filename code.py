"""
write a script that will ask for a string and tell if a letter in the string is vowel or consonant
"""

"""
my_string=input('please enter a world:  ').strip()
for i in my_string:
    if i in 'aeiou':
        print(f"{i} is a vowel")
    else:
        print(f"{i} is a consonant")"""

my_string=input('please enter a world:  ').strip()
num_c=0
num_v=0
for i in my_string:
    if i in 'aeiou':
        num_c+=1
print(f"number of vowel is:{num_v}") 
print(f"number of consonant is:{num_c}")   