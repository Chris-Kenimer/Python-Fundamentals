import random
i = 1
heads = 0
tails = 0
for i in range(0,5001):
    random_num = random.random()
    if round(random_num) == 1:
        print "Attempt #"+ str(i)+" Throwing a coin.... It's a head! .... Got "+ str(heads) +" head(s) so far and "+ str(tails) +" tail(s) so far"
        heads += 1
    elif round(random_num) == 0:
        print "Attempt #"+ str(i) +" Throwing a coin.... It's a tail! .... Got "+ str(heads) +" head(s) so far and "+ str(tails) +" tail(s) so far"
        tails += 1
print "Ending the program, Thank You!"
