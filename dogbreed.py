#Mya Maher
#Dog Breed
#This program will help the user pick a dog breed they would like to adopt that fits their daily life

#Init
import pandas as pd
import webbrowser


data = pd.read_csv('Mya Maher - dogs - Sheet1.csv')


name = data['Name'].tolist()
min_weight = data['Minimum Weight'].tolist()
max_weight = data['Maximum Weight'].tolist()
temperament = data['Temperament'].tolist()
purpose= data['BredFor'].tolist()
image = data['Image'].tolist()
breed = []
bred = []

#Init
def dogsize():
    size = input("What dog size do you prefer? (tiny, small, medium, large) ")


    if size == "tiny":
        for i in range(len(name)):
            if max_weight[i] <= 10:
                breed.append(name[i])
        print(breed)
        breed.clear


    elif size == "small":
        for i in range(len(name)):
            if max_weight[i] <= 25 and min_weight[i] >= 11:
                breed.append(name[i])
        print(breed)
        breed.clear


    elif size =="medium":
        for i in range(len(name)):
            if max_weight[i] <= 60 and min_weight[i] >= 26:
                breed.append(name[i])
        print(breed)
        breed.clear


    else:
        for i in range(len(name)):
            if max_weight[i] <= 60:
                breed.append(name[i])
        print(breed)
        breed.clear


def temp():
    breed_name = input("What temperment do you want your dog to be? ")
    number = 0
    for i in range(len(name)):
        if breed_name in name[i]:
            print("This dog is known for being:")
            print(temperament[i])
            webbrowser.open(image[i])
            number = number + 1

def make():
    made = input("What do you want your dog to be bred for? ")
    for i in range(len(purpose)):
        if made in purpose[i]:
            bred.append(purpose[i])
    print(bred)
    bred.clear()

def menu():
    dogsize()
    temp()
    make()
#Functions
menu()

#Main

#Sources
#Mr.J shared this data with me.



