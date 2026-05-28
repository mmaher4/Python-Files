#Mya
#Nicknames
#Generates a princess name based off of questions
def princess():
    story = input("Would you like a personal growth story or a romance based story? ")

    if story == "personal growth":
        mood = input("Now choose if you are more determined or calm: ")

        if mood == "determined":
            adventure = input("Are you adventurous or laid back? ")

            if adventure == "adventurous":
                print("You are most similar to Anna!")
            elif adventure == "laid back":
                print("You are most similar to Snow White!")

        elif mood == "calm":
            enjoy = input("Do you prefer water or ice? ")

            if enjoy == "water":
                print("You are most similar to Moana!")
            elif enjoy == "ice":
                print("You are most similar to Elsa!")

    elif story == "romance":
        personality = input("Are you more outgoing or kept to yourself? ")

        if personality == "outgoing":
            theme = input("Do you prefer an action filled plot or peaceful? ")

            if theme == "action filled":
                print("You are most similar to Mulan!")
            elif theme == "peaceful":
                print("You are most similar to Jasmine!")

        elif personality == "kept to myself":
            hobby = input("Do you prefer reading or singing? ")

            if hobby == "reading":
                print("You are most similar to Belle!")
            else:
                print("You are most similar to Ariel!")
princess()
