#Taylor Mendes
"""
This program is a quiz about women's gymnastics. It is a set of 10 questions including true/false questions, multiple choice questions, numeric response, and
fill in the blank. You will have two guesses at each question with the second guess being worth half of the points. You will not get two attempts for true/false questions.
The program will then calculate and output your grade numerically and as a letter. 
Algorithm 
1.	Initialize The variable total Score to zero
2.	Print question 1 (numerical answer)
3.	Receive integer input from user and name it q1
4.	Use if/else statement - if q1 == 16, print “good job that’s correct” and add one point to the variable totalScore.
5.	Else, print “sorry that’s wrong, try again”
6.	For the second attempt - Within the ‘else’ section of the previous if/else statement - create another if/else statement -  if q1 == 16  print “good job that’s correct” and add half a point to the variable totalScore.
7.	Else - print “Sorry that's wrong”
8.	Print question 2 (True or False)
9.	Take input from the user that is either ‘True’ or ‘False’ and label it q2
10.	Use if/else statement that if  q2 == ‘True’ then print “good job that's correct and add one to totalScore, else print “sorry that’s wrong
11.	Print question 3 (multiple choice) 
12.	Print the options for the answer (Vault, Rings, Bars, Floor) as a, b, c, or d using \n for the newline between each one. 
13.	Take user input for the answer as a, b, c, or d  and label it q3
14.	Use if/else statement where if q3 == b  then print “Good job that’s correct and add one to the variable totalScore
15.	Else - print “sorry that’s wrong, try again.”
16.	For the second attempt - Within the ‘else’ section of the previous if/else statement - create another if/else statement -  if q3 == b  print “good job that’s correct” and add half a point to the variable totalScore.
17.	Else - print “Sorry that's wrong”
18.	Print question 4 (multiple choice) 
19.	Print the options for the answer (Aly Raisman, Simone Biles, Laurie Hernandez, Gabby Douglas) as a, b, c, or d using \n for the newline between each one. 
20.	Repeat steps 13 through 17(multiple choice) for question 4 adding extra options if necessary 
21.	Print question 5 (multiple choice) 
22.	Print the options for the answer (Firecracker, Flying Squirrel, Tater Tot,) as a, b, or c,using \n for the newline between each one. 
23.	Repeat steps 13 through 17 (multiple choice) for question 5, adding extra options if necessary
24.	Print question 6 (fill in the blank)
25.	Take user input of a word and label it q6 
26.	Use if/else statement where if q6 == ‘rhythmic’ then print “Good job that’s correct” and add one to totalScore. Else print “Sorry that’s incorrect, try again”
27.	For the second attempt - Within the ‘else’ section of the previous if/else statement - create another if/else statement -  if q6 == ‘rhythmic’  print “good job that’s correct” and add half a point to the variable totalScore.
28.	Else - print “Sorry that's wrong”
29.	Print question 7 (True or False)
30.	Take input from the user that is either ‘True’ or ‘False’ and label it q7
31.	Use if/else statement that if  q7 == ‘True’ then print “good job that's correct and add one to totalScore, else print “sorry that’s wrong
32.	Print question 8 (Numerical)
33.	Repeat steps 3 - 7 (numerical) and change “q1 into q8” and change 16 into 1928
34.	Print question 9 (True or False)
35.	Take input from the user that is either ‘True’ or ‘False’ and label it q9
36.	Use if/else statement that if  q9 == ‘True’ then print “good job that's correct and add one to totalScore, else print “sorry that’s wrong
37.	Print question 10 
38.	Repeat steps 3 - 7 (numerical) and change “q1 into q10” and change 16 into 4
39.	Print total score/10
40.	Calculate percentage score by multiplying total score * 10 
41.	Use if/ elif/ elif/ elif/ else statement to calculate letter grade ( >= 90 is A, < 90 and >=80 is B, <80 and >= 70 is C, <70 and >=60 is D, <60 is an F
42.	Print letter grade. """ 
  



print("Hello welcome to the quiz, the topic is womens gymnastics")
print("You will get two attempts for each question (except true or false) and will recieve half points if you get it right on the second attempt")

totalScore = 0
# Question 1 
print("Question 1")
print("How many gymnasts are currently on the US gymnastics team?")
q1 = float(input("Enter an integer"))
if q1 == 16:
    print("Good Job that's correct")
    totalScore += 1
else:
    print("Sorry that's wrong, try again")
    q1B = float(input("Enter answer"))
    if q1B == 16:
        print("Good Job that's correct")
        totalScore += .5
    else:
        print("Sorry that's wrong")
        print("Correct answer is 16")

# Question 2
print("Question 2")
print("True or False - Simone Biles is registered to compete in the next Olympics tournament")
q2 = int(input("Enter answer as 1 for True' or 2 for False"))
if q2 == 1:
    print("Good Job that's correct")
    totalScore += 1
else:
    print("Sorry that's incorrect")
    print("Correct answer is True")


# Question 3
print("Question 3")
print("Which of the following is NOT a women's gymnastics event?")
print("a)Vault \nb)Rings \nc)Bars \nd)Floor \ne)Beam")
q3 = input("Enter answer as a, b, c, d, or e")
if q3 == 'b':
     print("Good Job thats correct")
     totalScore += 1
else:
    print("Sorry thats wrong, try again")
    q3B = input("Enter answer as a, b, c, d, or e")
    if q3B == 'b':
        print("Good Job thats correct")
        totalScore += .5
    else:
        print("Sorry thats wrong")
        print("Correct answer is b")
        
#Question 4
print("Question 4")
print("Who was the first Black gymnast to win a gold medal all-around")
print("a)Aly Raisman \nb)Simone Biles \nc)Laurie Hernandez \nd)Gabby Douglas")
q4 = input("Enter answer as a, b, c, or d")
if q4 == 'd':
     print("Good Job thats correct")
     totalScore += 1
else:
    print("Sorry thats wrong, try again")
    q4B = input("Enter answer as a, b, c, or d")
    if q4B == 'd':
        print("Good Job that's correct")
        totalScore += .5
    else:
        print("Sorry thats wrong")
        print("Correct answer is d")
        
#Quetsion 5
print("Question 5")
print("What was Gabby Douglas' nickname when she competed?")
print("a)Firecracker \nb)Flying Squirrel \nc)Tater Tot")
q5 = input("Enter answer as a, b, or c")
if q5 == 'b':
    print("Good Job that's correct")
    totalScore += 1
else:
    print("Sorry that's wrong, try again")
    q5B = input("Enter answer as a, b, or c")
    if q5B == 'b':
        print("Good Job, that's correct")
        totalScore += .5
    else:
        print("Sorry that's wrong")
        print("correct answer is b")
        

# Question 6
print("Question 6")
print("--blank--- gymnastics is the kind with hula hoops and ribbons")
q6 = input("Enter answer as a word to fill in the blank")
if q6 == 'rhythmic':
     print("Good Job that's correct")
     totalScore += 1
else:
    print("Sorry that's wrong, try again")
    q6B = input("Enter answer as a word to fill in the blank")
    if q6B == 'rhythmic':
        print("Good Job, that's correct")
        totalScore += .5
    else:
        print("Sorry that's wrong")
        print("Correct answer is rhythmic")


# Question 7 
print("Question 7")
print("True or False- the word Gymnastics comes from the Greek word to exercise naked")
q7 = int(input("Enter 1 for True or 2 for False"))
if q7 == 1:
    print("Good Job that's correct")
    totalScore += 1
else:
    print("Sorry that's incorrect")
    print("Correct answer is True")

# Question 8
print("Question 8")
print("What year were women allowed to do competetive gymnastics")
q8 = float(input("Enter year as an integer"))           
if q8 == 1928:
    print("Good job that's right")
    totalScore += 1
else:
    print("Sorry thats wrong, try again")
    q8B = input("Enter year as an integer")
    if q8B == '1928':
        print("Good Job that's correct")
        totalScore += .5
    else:
        print("Sorry thats wrong")
        print("Correct answer is 1928")
     
#Question 9
print("Question 9")
print("True or False - Young gymnasts are more likely to be injured than football players")
q9 = input("Enter 1 for True or 2 for False")
if q9 == 1:
     print("Good Job that's correct")
     totalScore += 1
else:
    print("Sorry that's incorrect")
    print("Correct answer is True")
    
#Question 10
print("Question 10")
print("How many events are there in womens gymnastics")
q10 = int(input("Enter integer"))
if q10 == 4:
    print("Good Job that's correct")
    totalScore += 1
else:
    print("Sorry that's wrong, try again")
    q10B = input("enter integer")
    if q10B == 4:
        print("Good Job, that's correct")
        totalScore += .5
    else:
        print("Sorry that's wrong")
        print("correct answer is 4")
        
    
print("Your total score is", totalScore,"/10")
percentageScore = totalScore * 10
print("Your percentage score is", percentageScore,"%")
if percentageScore >= 90:
    print("Great work! You recieved an A! You'd make a great gymnast!")
elif percentageScore < 90 and percentageScore >= 80:
    print("Nice work you know a lot about gymnastics! you recieved a B")
elif percentageScore < 80 and percentageScore >= 70:
    print("There's Room for improvement, you recieved a C")
elif percentageScore < 70 and percentageScore >= 60:
    print("Keep trying, you recieved a D")
else:
    print("You should learn some more about gymnastics. You recieved an F")
    



        
        
    
    
    
