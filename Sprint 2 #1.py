#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import random

question = input('Would you like to roll the dice [Y/N]?\n')

while question != 'N':
    if question == 'Y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
        question = input('Would you like to roll the dice [Y/N]?\n')
    else:
        print('Invalid response. Please type "Y" or "N".')
        question = input('Would you like to roll the dice [Y/N]?\n')        

print('Good-bye!')


# In[ ]:





# In[ ]:





# In[ ]:




