####################### DO NOT MODIFY THIS CODE ########################
# Use this function to calculate the total of your order
def get_total_price(order_list):
	order_total = 0
	for order in order_list:
		if order.lower() in original_flavors:
			order_total += original_price
		else:
			order_total += signature_price
	return order_total

menu = {
	"Original Cupcake": 2,
	"Signature Cupcake": 2.750,
	"Coffee": 1,
	"Tea": 0.900,
	"Bottled Water": 0.750
}
original_flavors = ["Vanilla", "Chocolate", "Strawberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = #complete me!
signature_flavors = #complete me!
"""
complete me!
"""
order_list = #complete me!

# If the total is 20 KD or above, that means we can accept the credit card for payment
# In that case return True, to indicate that for this total price a credit card CAN be used for payment.
# If the total is less than 20 KD, that means we can't accept the credit card for payment
# In that case return False, to indicate that for this total price a credit card CANNOT be used for payment.
def accept_credit_card(total):
	#complete me!


# 1) Print the menu and the prices of all the items in a nice readable format.
# 2) Print the following message:
	# "Let me repeat your order, sir/ma'am."
# 3) Print the order list.
# 4) Then print the following message:
	# "That'll be <PRICE_HERE> KD."
# 5) Check the total price of the order, if credit card is acceptable print:
	# "You can pay with credit card if you want!"
# 6) Lastly, print "Thank you for shopping at <CUPCAKE_SHOP_NAME>"
