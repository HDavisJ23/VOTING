var1 = True
while var1 == True:
    name = input("What is your name: ")
    age = input("How old are you: ")
    age = int(age)
    party =  input("What is your political party: ")
    decision = input("So are you going to vote: ")

    def Politics(n,a,p,d):
        print(f" \nGood Day {n} !\n")
        print(f"Oh wow so you are {a} years old !\n")
        if a < 18:
            print("Dang your not old enough to vote !!!.\n")
        else:
            print("You can vote !!!\n")
        print("So your a ", p," huh. \n")
        print ("You told me your decision is", d,"\n")
        choice = input("Is your choice the same: ")


    Politics(name,age,party,decision)

    Question = input("Are you finised the poll survey (Answer with a YES or NO): ")
    if Question == "YES":
        var1 = False
