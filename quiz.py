def qna():
    questions=("1. Which animal is known as the 'Ship of the Desert'?",
               "2. How many days are there in a week?",
               "3. How many hours are there in a day?",
               "4. How many letters are there in the English alphabet?",
               "5. Rainbow consist of how many colours?")
    options =(("A. Cow","B. Dog","C. Camel","D. Snake"),
              ("A. 5","B. 7","C. 13","D. 10"),
              ("A. 27","B. 24","C. 26","D. 23"),
              ("A. 26","B. 21","C. 25","D. 30"),
              ("A. 5","B. 3","C. 9","D. 7"))
    answers=("C","B","B","A","D")
    quiz(questions,options,answers)



def quiz(questions,options,answers):
    guesses = []
    score = 0
    question_num = 0
    for question in questions:
        print("\n")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter (A ,B ,C ,D): ").upper()
        guesses.append(guess)
        if guess==answers[question_num]:
            print("CORRECT!")
            score+=1
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} was the correct answer.")
        next=input("Press Enter to continue.")
        question_num+=1
    score = (score/len(questions))*100
    print(f"Your score = {score}%")
    return score
qna()