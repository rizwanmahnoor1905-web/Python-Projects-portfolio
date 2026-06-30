import random
choice=['rock','paper','scissor']
user_choice=input('enter your choice').lower()
if user_choice in choice:
       print(f"computer choice is {random.choice(choice)}")
