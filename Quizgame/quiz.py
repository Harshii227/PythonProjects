questions = ("how many elemnts are in the periodic table?: ",
             "which animal lays the largest aggs?:" ,
             "what is the most abundent gas in Earth's atmosphere?:" ,
             "how many bones are in the human body?:" ,
             "which planet in the solar system the hottest?:")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A, Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question__num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")    
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("------------------------------")
print("           RESULTS             ")
print("------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()    


print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score}%")




