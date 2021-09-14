
#Iterate over list
list = [1, 2, 3, 4, 5]

Iterator = iter(list)

for x in Iterator:
    print(x)

######################
#Role dice
from random import *

def roll_dice():
    return randint(1,6)

my_iter = iter(roll_dice, 6)
for x in my_iter:
    print("Dice roll", x)
print("Yay! Dice roll", 6)    


#######################


