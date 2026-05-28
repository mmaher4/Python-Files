#Mya Maher
#Grocery Store
#Contains functions for running a grocery store
#Init
items = [
    "Milk", "Eggs", "Bread", "Butter", "Cheese",
    "Chicken Breast", "Ground Beef", "Pork Chops", "Bacon", "Sausage",
    "Pasta", "Rice", "Quinoa", "Cereal", "Oatmeal",
    "Apples", "Bananas", "Oranges", "Strawberries", "Blueberries",
    "Grapes", "Pineapple", "Mangoes", "Lemons", "Limes",
    "Potatoes", "Onions", "Garlic", "Carrots", "Broccoli",
    "Cauliflower", "Spinach", "Kale", "Lettuce", "Bell Peppers",
    "Tomatoes", "Cucumbers", "Zucchini", "Mushrooms", "Avocados",
    "Olive Oil", "Vegetable Oil", "Cooking Spray", "Salt", "Pepper",
    "Sugar", "Brown Sugar", "Flour", "Baking Powder", "Baking Soda",
    "Peanut Butter", "Jelly", "Honey", "Maple Syrup", "Nutella",
    "Coffee", "Tea", "Hot Chocolate", "Creamer", "Sugar Packets",
    "Orange Juice", "Apple Juice", "Soda", "Sparkling Water", "Sports Drink",
    "Chips", "Crackers", "Pretzels", "Popcorn", "Cookies",
    "Ice Cream", "Frozen Pizza", "Frozen Vegetables", "Frozen Chicken Nuggets", "Frozen Waffles",
    "Canned Soup", "Canned Beans", "Canned Corn", "Canned Tomatoes", "Canned Tuna",
    "Ketchup", "Mustard", "Mayonnaise", "BBQ Sauce", "Hot Sauce",
    "Paper Towels", "Toilet Paper", "Facial Tissues", "Dish Soap", "Laundry Detergent"
]

prices = [
    3.49, 2.99, 2.79, 3.99, 4.59,
    7.99, 6.49, 5.99, 4.99, 4.49,
    1.79, 4.29, 5.99, 3.99, 3.49,
    4.49, 1.39, 3.99, 4.99, 5.49,
    5.49, 3.49, 4.99, 1.79, 1.79,
    3.99, 2.49, 1.29, 2.29, 2.99,
    3.49, 3.49, 3.99, 2.49, 3.49,
    2.99, 1.79, 2.49, 2.99, 1.99,
    7.99, 5.49, 3.99, 1.29, 2.49,
    2.49, 2.99, 3.49, 2.49, 1.99,
    3.99, 3.29, 4.99, 6.99, 5.49,
    9.99, 4.49, 3.99, 2.49, 1.99,
    4.29, 3.99, 1.99, 2.49, 2.99,
    3.99, 3.49, 2.99, 2.49, 4.99,
    5.99, 6.49, 2.99, 7.49, 4.99,
    2.79, 1.49, 1.29, 1.79, 2.49,
    2.99, 2.49, 4.49, 3.49, 3.99,
    8.99, 12.99, 3.99, 2.99, 11.99
]
def total():
#Asks for amount of money,shows what is available, and adds the total
    cart = 0
    while True:
        item_name = input("What do you want to buy? (nothing else): ")
        if item_name.lower() == "nothing":
            break

        item_list = item_name.split(",")
        i = 0
        while i < len(item_list):
            item = item_list[i].strip()
            price = get_price(item)
            if price is not None:
                cart += price
                #+= adds a value to another variable and reassigns it
            else:
                print(item, "not found")
            i += 1
            #Discount of 20%
        print("Total:", round(cart, 2))
    discount_total = cart * 0.8
    print("After your 20% discount your total is", round(discount_total, 2))



def get_price(item_name):
#Gets prices
    i=0
    while i <len(items):
        if items [i].lower()== item_name.lower():
            return prices[i]
        i += 1
    return None


def everything():
#Ties it all together
    max_price=float(input("How much money do you have? "))
    i = 0
    print("You can buy: ")
    while i < len(prices):
        if prices[i]<= max_price:
            print(items[i], "-", prices[i])
        i+=1
    total()

def final():
    get_price("Butter")
    everything()


final()
#Creates the final grocery store!
