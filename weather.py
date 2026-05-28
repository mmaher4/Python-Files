#Mya M
#Weather
#Tells you clothing to wear depending on weather
def weather():
    weather = int(input("Please enter temperature: "))
    if weather <= 60:
        print("It's cold so wear a jacket, pants, gloves, and hat!")
    elif weather <= 75:
        print("It's chilly so wear a shirt, hoodie,and pants!")
    else:
        print("It's warm so wear a t-shirt, shorts, and possibly sunglasses!")

weather()
