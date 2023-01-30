n = input("Enter a noun ")
v = input("Enter a verb ")
av = input("Enter an adverb ")
noa = int(input("How many adjectives would you like? "))

aa = []
#empty sqaure brackets for where the adjectives go
for i in range(noa):
    a = input("Add an adjective ")
    aa.append(a)
    #note aa and a are different variables. Important for the sentence
print("The "+", ".join(aa)+ " "+n+" "+v+" "+av+" at the character.")
#the + .join(aa)+ joins the adjectives to the sentence and ", " leaves
#a comma and space between every adjective except the last one, which
#only leaves a space.
