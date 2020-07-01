import random   # import random functionality

rndInt = random.randrange(100)      # Generate random number between 0 and 100
guess = 101                         # placeholder for guess of user

print("I'd like to play a game, bet you can't guess the number im thinking of? Aight, try your luck!")

while rndInt != guess:              # while generated number is not equal to guess    
    guess = int(input("Guess?"))    # get user input
    if guess < rndInt:              
        print ("nah, too small, try again.")   
    elif guess > rndInt:
        print ("Really? Too large my friend.")      
    if guess == rndInt:
        break
        
print("Yep! You're right. Good job")
        