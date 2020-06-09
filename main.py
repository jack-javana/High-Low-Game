import random

print ("High low game")

print ("1. Manual start\n2. Random start")
# GameStart variable is mode select
GameStart = int(input())

if GameStart == 1:
    print ("input number for game")
    Number = int(input())

if GameStart == 2:
    # Random number is chosen
    Number = random.randint(0, 100)

# Infinite cycle 
while 1:
    inputt = input("High-Low: ")
    if int(inputt) == Number:
        print("You Win")
        break
    elif int(inputt) > Number:
        print("Number is lower")
        continue
    elif int(inputt) < Number:
        print("Number is higher")
        
exit()
