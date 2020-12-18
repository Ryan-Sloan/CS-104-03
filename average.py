numberofscores = 0
score = 0
total = 0
average = 0.0
scorecount = 0
numberofscores= int(input("please enter the number of scores you want to average: "))

#counting loop using while
print ("counting loop using while")
x=1
while x <= 10:
    print("x= ",x)
    x = x+1
print()

#what python loop sctructure could we use to repeat the next 3 lines
score = int(input("Please enter a score: "))
total = total + score 
scoreCount = scoreCount + 1


average = total / numberOfScore
print(average)
