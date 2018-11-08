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
    founded = 0
    for item in menu:
        if item == order:
            founded = 1

    for item in original_flavors:
        if item == order:
            founded = 1
            break

    for item in signature_flavors:
        if item == order:
            founded = 1
            break

    if founded == 1:
        return True
    else:
        return False

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    print ("Welcome to %s , Enter your order exactly \
as you see in the menu. whenever you done, type 'Exit' " %cupcake_shop_name)
    user_input = input()
    while user_input != "Exit":
        if is_valid_order(user_input):
            order_list.append(user_input)
            user_input = input()
        else:
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
        for key in menu:
            if key == item:
                total = total + menu[key]
                break

    for i in order_list:
        for j in original_flavors:
            if i == j:
                total = total + original_price
                break

    for i in order_list:
        for j in signature_flavors:
            if i == j:
                total = total + signature_price
                break

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for i in order_list:
        print ("- %s" %i)
    print ("that will be KD %s" % get_total_price(order_list))
    accept_credit_card(get_total_price(order_list))
    print ("Thanks for shopping at %s" %cupcake_shop_name)


