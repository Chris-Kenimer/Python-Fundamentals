def scoreInput():
    response = raw_input("Please enter a score: ")
    return response
def scoreEval(value):
    if int(value) in range(59,70):
        print "Score: " + str(value) + "; Your grade is D"
    elif int(value) in range(69,80):
        print "Score: " + str(value) + "; Your grade is C"
    elif int(value) in range(79,90):
        print "Score: " + str(value) + "; Your grade is B"
    elif int(value) in range(89,101):
        print "Score: " + str(value) + "; Your grade is A"
scores = []
i = 0
for i in range(0,10):
    scores.append(scoreInput())

print "Scores and Grades"
for value in scores:
    scoreEval(value)

print "End of the program. Bye!"
