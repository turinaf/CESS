score = int(input("Enter score: "))

if (score >90 and score <100):
    print("Excellent")
elif (score>75 and score <90):
    print('Good')
elif (score >= 60 and score <75):
    print("Passed")
elif (score<60 and score>0):
    print("Fialed")
else:
    print("Unknown input")
