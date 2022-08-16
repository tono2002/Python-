import random

print("Adivina el número entre 0 y 5000")
r = random.randrange(0, 5001)

while True:        
    guess = int(input("Adivina: "))
    if guess > r:
        print("Muy alto")
    elif guess < r:
        print("Muy bajo")
    else:
        print("Correcto!")
        break
print("Me gusta beber matarratas")









