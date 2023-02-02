import random

loop = False
while loop == False:
    q = input("Would you like to play a custom story or a randomised tale? ").capitalize()

    if q == "Custom story" or q == "Custom Story" or q == "Custom":
        n = input("Enter a noun ")
        v = input("Enter a verb ")
        av = input("Enter an adverb ")
        noa = int(input("How many adjectives would you like? "))

        aa = []
        #empty square brackets for where the adjectives go
        for i in range(noa):
            a = input("Add an adjective ")
            aa.append(a)
            #note aa and a are different variables. Important for the sentence
        print("The "+", ".join(aa)+ " "+n+" "+v+" "+av+" at the character.")
        #the + .join(aa)+ joins the adjectives to the sentence and ", " leaves
        #a comma and space between every adjective except the last one, which
        #only leaves a space.


    elif q == "Rt" or q == "Randomised tale" or q == "Randomised Tale" or q == "Random":
        nlist = "person", "boar", "bull", "anaconda", "titan"

        n = random.choice(nlist)
        vlist = "danced", "lunged", "attacked", "rushed", "killed"
        v = random.choice(vlist)

        
        if v == "danced":
            con = str("towards ")
        elif v == "lunged" or v == "rushed":
            con = str("at ")
        else:
            con = str("")

        print("The "+n+" "+v+" "+con+"the character.")
        endloop = input("Would you like to end the program? ").capitalize()
        if endloop == "Yes":
            print("Have a good day ")
            loop = True
        else:
            print("Okay ")
            
    else:
        print("That is not an option, please try again.")
