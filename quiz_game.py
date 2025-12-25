print("Welcome to the Quiz Game!")

playing = input("Do you want to play ? (yes/no): ")     # asking if the user want to play the game or not
if playing == "yes":                # if the user wants to play the game 
    print("Great! Let's start the game.")

    score = 0       # intial score of the user 

    ans = input("What is the full form of CPU? :")          # first question 
    if ans.lower() == "central processing unit":
        print("Correct!")
        score +=1
    else:
        print("Wrong! The correct answer is Central Processing Unit.")

    ans = input("What is the full form of RAM? :")          # second question
    if ans.lower() == "random access memory":
        print("Correct!")
        score +=1
    else:
        print("Wrong! The correct answer is Random Access Memory.")

    ans = input("What is the full form of GPU? :")          # third question
    if ans.lower() == "graphics processing unit":
        print("Correct!")
        score +=1
    else:
        print("Wrong! The correct answer is Graphics Processing Unit.")

    ans = input("What is the full form of HTML? :")             # fourth question
    if ans.lower() == "hypertext markup language":
        print("Correct!")
        score +=1
    else:
        print("Wrong! The correct answer is Hypertext Markup Language.")   

    print("You got " + str(score) + " questions correct!")      # showing the final score of the quiz to the user
    print("That is:", (score/4) * 100, "%")             # showing the user's percentage score

else:
    print("Maybe next time!")           # if the user does not want to play the game 
    quit()