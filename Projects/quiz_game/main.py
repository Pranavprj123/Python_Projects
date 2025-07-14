print("Welcome to the Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()   

print("Okay! Let's start the game :)")
score = 0

answer = input("Q1) What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect! The correct answer is 'Central Processing Unit'.")

answer = input("Q2) What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Paris'.")

answer = input("Q3) What is 2 + 2? ")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is '4'.")

answer = input("Q4) What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Jupiter'.")
answer = input("Q5) Who wrote 'Romeo and Juliet'? ")
if answer.lower() == "william shakespeare":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'William Shakespeare'.")
print("Thanks for playing the Quiz Game!")
print("You answered", score, "questions correctly.")