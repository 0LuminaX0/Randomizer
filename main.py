# The start of the file

from random import randint
from time import sleep
from os import system


for i in range(10):
    system("cls")
    print(randint(0, 9))
    sleep(0.1 * i)

# The end of the file
