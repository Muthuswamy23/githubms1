import random

print(random.randint(1,10))    #output 1 to 10
print(random.randrange(1,10))  #output 1 to 9


#float
print(random.random())  
print(random.uniform(1,9))  


alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(random.choice(alphabets))
print(random.choices(alphabets,k=27))   # with duplicates
print(random.sample(alphabets, 2))       #without duplicates



#shuffling
L=["1","2","3","4","5"]
random.shuffle(L)
print(L)


#seeding
random.seed(55)
print(random.randint(1, 100))


#exammple 1: simple dice game
 
def roll_dice():
    return random.randint(1,6)

for i in range(5):
    print("ROLL:",roll_dice())



#password generator
import random
import string
char=string.ascii_letters + string.digits + "!@#$%^&*"
password=""
for i in range(5):
   password +=random.choice(char)
print(password)