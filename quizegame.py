print("WELL COME TO QUIZE GAME")
questions=("1.how many elements are in periodic table?:",
           "2.what is name of capital city of india?:",
           "3.who is invented python progamming language?:",
           "4.what is the maximum length of a python identifier?:",
           "5.how is a code block indetation in python?:",
           "6.which of the following conceptd is not a part of python?:")
options=(("A.115","B.114","C.118","D.114"),
         ("A.DEHLI","B.PANJAB","C.HARIYANA","D.NOIDA"),
         ("A.dennis M.ritchie","B.James Gosling","C.gard vinch","D.guido van Rossum"),
         ("A.34","B.21","C.No fixed length is specified","D.14"),
         ("A.Brackets","B.Indentation","C.Key","D.No of the above"),
         ("A.Pointers","B.Loops","C.Dynamic Typing","D.All of the above"))
answers=("C","A","D","C","B","A")
guesses=[]
score=0
question_no=0
for question in questions:
    
    print(".......................")
    print(question)
    for option in options[question_no]:
        print(option)
    guess =input("enter(A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_no]:
        score += 1
        print("correct!")
    else:
        print("incorrect!")
        print(f"{answers[question_no]} is the correct answer")
    question_no += 1
    
print("---------------------------------")
print("     RESULTS     ")
print("---------------------------------")

print("answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score = (score / len(questions)*100)
print(f"Your score is :{score}%") 
