cartItems = []

def showOption():
    print("""
        Press 1 to view show cart items
        Press 2 to add new item into cart
        Press 3 to delete item from cart
        Press 4 to exit from app
    """)
    userSelect = int(input("Enter your option : "))

    if(userSelect == 1):
        viewCartItems()
    elif(userSelect == 2):
        addItemIntoCart()
    elif(userSelect == 3):
        deleteItemFromCart()
    elif(userSelect == 4):
        exit()
    else:
        print("Invalid option entered, Please try again")
        showOption()


def viewCartItems():
    if len(cartItems) == 0:
        print("Cart is empty")
    else:
        print(cartItems)
    """    
    else:
        for x in cartItems:
            print(x)
    """

    showOption()

def addItemIntoCart():
    itemName = input("Enter Item Name : ")
    cartItems.append(itemName)
    print("Item added successfully into the cart")
    showOption()

def deleteItemFromCart():
    itemName = input("Enter Item Name : ")
    cartItems.remove(itemName)
    print("Item successfully remove from the cart")
    showOption()

def wantToContinue():
    print("""
            Press 0 to show all options
            Press 4 to exit from app
        """)

    userSelect = int(input("Enter your option : "))

    if(userSelect == 0):
        showOption()
    elif(userSelect == 4):
        exit()
    else:
        print("Invalid option entered, Please try again")
        wantToContinue()

showOption()
