print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the color of rose? ")
if answer.lower() == "red":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What is the IPS called? ")
if answer.lower() == "indian police service":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Tell me the full form of ML? ")
if answer.lower() == "machine learning":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("Your score: " + str((score / 4) * 100) + "%")
