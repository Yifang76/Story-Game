import random

loop = False
while loop == False:
    
    q = input("Would you like to play a custom story or a randomised tale? ").capitalize()
    if q == "Rt":
        n = random.randint(1,5)
        def noun(number, noun):
            n = random.randint(1,5)
            #if n == number:
            n = str(noun)

        noun(1, "person")
        n = str(n)
        v = str("b")
        print("The "+n+" "+v+" at the character.")

    else:
        print("That is not an option, please try again.")

# def sentence(mainClause, subClause):
#   print("mainClause, subClause)
#sentence(random.choice(["dog","cat"]),random.choice(["jump","leak"]))
