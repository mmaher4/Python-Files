#Mya Maher
#MADLIBS
#Creates an interactive story
#Gather input
def madlibs():
    import random
    BOLD = '\033[1m'
    END = '\033[0m'
    print("Welcome to MADLIBS, have fun!")
    location = input("Pick a location: ")
    location = location.upper()
    if location == "random":
        place = ["Mall", "Grocery Store","Living room", "School","Playground"]
        random_item = random.choice(place)
        random_item = random_item.upper()
        print (random_item)
    item = input("What item are you looking for there: ")
    item = item.upper()
    if item == "random":
        things = ["Rocks", "Cheese", "Cardboard", "Sock", "Pillow"]
        random_item = random.choice(things)
        random_item = random_item.upper()
        print(random_item)
    suprise = input("What did you find while looking for the item: ")
    suprise = suprise.upper()
    if suprise == "random":
        secret = ["Salad", "Quarter", "Used pencil", "Shirt", "Her Wallet"]
        random_item = random.choice(secret)
        random_item = random_item.upper()
        print(random_item)
    emotion = input("How do these items make you feel: ")
    emotion = emotion.upper()
    if emotion == "random":
        feel = ["Sad", "Angry", "Disappointed", "Excited", "Gloomy"]
        random_item = random.choice(feel)
        random_item = random_item.upper()
        print(random_item)
        #Story
    print(f"""I went to the {BOLD}{location}{END} with my sister.
We ran around looking for a {BOLD}{item}{END}, because it's for our mom's birthday gift.
We also secretly suprised her with a {BOLD}{suprise}{END}.
When she seen what we got she felt so {BOLD}{emotion}{END}!
    """)




madlibs()
