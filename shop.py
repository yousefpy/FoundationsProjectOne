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
cupcake_shop_name = "Coffee Tarven"
signature_flavors = ["Slice of life" , "Piece of Mind", "Yummy Tummy"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print ("Our Menu:")
    for item in menu:
        print ("%s (%s)" % (item, menu[item]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for item in original_flavors:
        print (item)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for item in signature_flavors:
        print (item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in menu:
        return True
    elif order in original_flavors:
        return True
    elif order in signature_flavors:
        return True
    else:
        return False

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    #order_list = []
    print ("Welcome to %s , Enter your order exactly \
as you see in the menu. whenever you done, type 'Exit' " %cupcake_shop_name)
    user_input = input()
    while user_input.lower() != "exit":
        if is_valid_order(user_input):
            order_list.append(user_input)
            
        user_input = input()
    
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total >= 5:
        print ("Your order is eligible for credit card payment")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for item in order_list:
        #item = item.lower()
        if item in menu:
            total += menu[item]
        elif item in original_flavors:
            total += original_price
        elif item in signature_flavors:
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for i in order_list:
        print ("- %s" %i)
    total_price = get_total_price(order_list)
    print ("that will be KD %s." %total_price)
    accept_credit_card(total_price)
    print ("Thanks for shopping at %s." %cupcake_shop_name)


