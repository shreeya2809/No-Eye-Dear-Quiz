print("welcome to No Eye Dear Quiz")
answer=input('Are you ready to play the Quiz? (yes/no) :')

score=0

total_question=3

if answer.lower()=='yes': 
    answer=input('Question 1: In meter, how long is an olympic swimming pool? ')

if answer.lower()=='50': 
    score+=1
    print("correct")
else:
     print("Wrong Answer :(")

answer=input("Question 2: What year did the Berlin wall fall? ")

if answer.lower()=="1989":
   score+=1 
   print("correct")

else: 
    print("wrong Answer :(")

answer=input("Question 3: which is the most abundant element in the universe? ") 
if answer.lower()=="hydrogen":
   score+=1
   print('correct')

else: 
    print("Wrong Answer :(")

print("Thankyou for Playing to Eye Dear quiz game, you attempted", score, "questions correctly!")
mark=(score/total_question)*100
print("Marks obtained",mark)

print("BYE!")