#Mya Maher
#Bottles
#Prints lyrics to a song out
def song():
    num = int(100)
    for i in range(101):
        if num >1:
            print(f"{num} bottles of milk on the wall")
            print(f"{num} bottles of milk")
            num = int(num - 1)
            print("Take on down pass it around")
        elif num == 1:
            print("1 bottle of milk on the wall")
            print("1 bottle of milk")
            print("Take on down pass it around")
            num = int(num - 1)
        elif num < 1:
            print("No more bottles of milk on the wall!")
            print("Boo Hoo!")

song()
