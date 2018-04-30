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
cupcake_shop_name = "We don't Give A Fork"#complete me!
signature_flavors = ['teehee', 'vice']#complete me!
order_list = []

def print_menu():
	"""
	Print the items in the menu dictionary.
	"""
	print("Our menu:")
	for item in menu:
		print("- \"%s\" (KD %s)" % (item, menu[item]))

# your code goes here!
#------------------ START -------------------#
def print_originals():
	"""
	Print the original flavor cupcakes.
	"""
	print("Our original flavor cupcakes (KD %s each):" % original_price)
	for item in original_flavors:
		print("- \"%s\"" % item)
#------------------ FINISH -------------------#


#------------------ START -------------------#
def print_signatures():
	"""
	Print the signature flavor cupcakes.
	"""
	print("Our signature flavor cupcake (KD %s each):" % signature_price)
	for item in signature_flavors:
		print("- \"%s\"" % item)
#------------------ FINISH -------------------#

#------------------ START -------------------#
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
#------------------ FINISH -------------------#

#------------------ START -------------------#
# user input loop for order_list
def get_order():
	"""
	Repeatedly ask customer for order until they type "Exit".
	"""
	order_list = []
	order = input("What's your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order.)\n")
	while order.lower() != "exit":
		if is_valid_order(order):
			order_list.append(order)
		order = input()
	return order_list
#------------------ FINISH -------------------#


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

#------------------ START -------------------#
def print_order(order_list):
	"""
	Print the order of the customer.
	"""
	print()
	print("Your order is: ")

	# your code goes here!

#------------------ FINISH -------------------#
