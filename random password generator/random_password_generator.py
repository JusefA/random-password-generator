import string
from random import *

while True:
    letters = string.ascii_letters
    digits = string.digits 
    symbols = string.punctuation
    chars = letters + digits + symbols

    a = 8
    b = 16
    input("Press ENTER to generate a password")


    
    c = "".join(choice(chars) for x in range(randint(a,b)))
    print(c)
