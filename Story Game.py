import random
loop = False
while loop == False:
    
    q = input("Would you like to play a custom story or a randomised tale? ").capitalize()

    if q == "Custom Story" or q == "Custom story":
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

    elif q == "Randomised Tale" or "Randomised tale":
        n = random.randint(1,5)
        v = random.randint(1,5)
        av = random.randint(1,5)
        noa = random.randint(1,5)

        if n == 1:
            n = str("plane")
        elif n == 2:
            n = str("person")
        elif n == 3:
            n = str("building")
        elif n == 4:
            n = str("boar")
        elif n == 5:
            n = str("bull")

        if v == 1:
            v = str("glanced")
        elif v == 2:
            v = str("leaped")
        elif v == 3:
            v = str("jumped")
        elif v == 4:
            v = str("threw")
        elif v == 5:
            v = str("sprinted")

        if av == 1:
            av = str("gracefully")
        elif av == 2:
            av = str("flawlessly")
        elif av == 3:
            av = str("tauntingly")
        elif av == 4:
            av = str("violently")
        elif av == 5:
            av = str("dangerously")

        aa = []
        for i in range(noa):
            a = random.randint(1,5)
            if a == 1:
                a = str("golden")
            elif a == 2:
                a = str("mesmerizing")
            elif a == 3:
                a = str("extraordinary")
            elif a == 4:
                a = str("peerless")
            elif a == 5:
                a = str("flawless")
            aa.append(a)
        print("The "+", ".join(aa)+ " "+n+" "+v+" "+av+" at the character.")

    else:
        print("That is not an option, please try again.")
        
