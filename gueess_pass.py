import random

easy_words = ["train","apple","lion","money","india"]
medium_words = ["python","bottle","monkey","planet","laptop"]
hard_words = ["elephant","jaguar","diamond","umbrella","computer"]

print("WElcome to the Password Guessing Game!")
print("Choose your difficulty Level: Easy, Medium, Hard")

level = input("Choose your level: ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid Input. Default start you with Easy Level")
    secret = random.choice(easy_words)

attempts = 0
print("Guess the secret password: ")

while True:
    guess = input("Enter your guess: ").lower()
    attempts+=1

    if guess == secret:
        print(f"Congratulation you guess the password in {attempts} attempts")
        break
    
    hint =""

    for i in range(len(secret)):
        if i < len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+= "_"
    print("Hint: ", hint)
print("Game Over")
