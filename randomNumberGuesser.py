import random

# Write your code here.
# Make sure to use `random.randint` to pick your random number.

startNum = str()
endNum = str()
numGuesses = int()
guessedNum = None


while True:
    startNum = input("Enter the start of the range: ")

    if startNum.isdigit():
        startNum = int(startNum)
        break
    else: 
        print("Please enter a valid number.")

while True:
    endNum = input("Enter the end of the range: ")

    if endNum.isdigit():
        endNum = int(endNum)

        if endNum > startNum:
            break
        else: 
            print("Please enter a valid number.")
    else:
        print("Please enter a valid number.")

testedNum = random.randint(startNum, endNum)

while guessedNum != testedNum:
    choose = input("Guess a number: ")

    if choose.isdigit():
        guessedNum = int(choose)
        numGuesses += 1
    else: 
        print("Please enter a valid number.")
        continue



if numGuesses > 1:
    print(f"You guessed the number in {numGuesses} attempts")
else:
    print(f"You guessed the number in {numGuesses} attempt")