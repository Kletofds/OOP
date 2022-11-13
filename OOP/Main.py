#############################
# Dog/Cat generator
# Kelton Figurski
#############################

import Animals

import random
names = ["Max", "Bailey", "Bella", "Lucy", "Charlie", "Buddy", "Molly", "Daisy", "Rocky", "Sophie", "Jack" ]
colors = ["White", "Black", "Brown", "Grey"]

while True:

    dognum = input("How many dogs would you like to generate?")

    try:
        dognum = int(dognum)
        break

    except:
        print("Invalid Number")


while True:

    catnum = input("How many cats would you like to generate?")
    
    try:
        catnum = int(catnum)
        break
    
    except:
        print("Invalid Number")
        
print("\nDogs:\n")

while dognum > 0:
    name = random.choice(names)
    age = random.randint(1, 20)
    color = random.choice(colors)
    d = Animals.Dog(name, age, color)
    d.printchar()
    print("\n")
    dognum = dognum - 1
    
print("\nCats:\n")
    
while catnum > 0:
    name = random.choice(names)
    age = random.randint(1, 20)
    color = random.choice(colors)
    d = Animals.Cat(name, age, color)
    d.printchar()
    print("\n")
    catnum = catnum - 1