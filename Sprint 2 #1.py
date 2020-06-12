#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:

# Dice Rolling Simulator
import random

question = input('Would you like to roll the dice [Y/N]?\n')

while question != 'N':
    if question == 'Y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
        question = input('Would you like to roll the dice [Y/N]?\n') # User then chooses between Yes and No
    else:
        print('Invalid response. Please type "Y" or "N".') # If hypothetically user types a letter/digit thats not N or Y
        question = input('Would you like to roll the dice [Y/N]?\n')        

print('Good-bye!') # If the letter 'N' is used "Good-bye!" is printed


# In[ ]:





# In[ ]:





# In[ ]:




