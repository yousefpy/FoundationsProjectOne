####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Cup and Cake"
signature_flavors = ["Slice of life" , "Piece of Mind", "4get it"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print ("Our Menu:")
    for key,value in menu:
        print "%s (%s)," % (key, value)


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for item in original_flavors:
        print original_flavors[item],


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for item in signature_flavors:
        print signature_flavors[item],


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    founded = 0
    if menu.has_key(order):
        founded = 1
        break

    for item in original_flavors:
        if original_flavors[item] == order:
            founded = 1
            break

    for item in signature_flavors:
        if signature_flavors[item] == order:
            founded = 1
            break

    if founded =1:
        return True
    else:
        return False

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    print ("Welcome to Cup of Cake, Enter your order exactly\
     as you see in the menu. whenever you done, type 'Exit' ",)
    user_input = raw_input()
    while user_input != "Exit":
        if is_valid_order(user_input) == True:
            order_list.append(user_input)
            user_input = raw_input()
        else:
            user_input = raw_input()


    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
