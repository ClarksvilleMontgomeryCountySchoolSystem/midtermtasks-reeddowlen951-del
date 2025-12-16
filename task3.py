

# Testing flag - will be set by test
TESTING = True
item = None
price = None
quantity = None

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"

   Prosperity comes in threes!
========================================

ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
Flying Carpet...............$119.99
Phoenix Feather..............$14.99
Time Turner.....................$84.99
Enchanted Sword.................$65.99
Potion of Luck..................$11.99
Crystal Ball.....................$39.99
""")



# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)
def get_purchase_info():
    input('What is the item?')
    input('What is the price of the item?')
    input('What quantity of the item did you buy?')
    return item, price, quantity
int('item')
int('price')
int('quantity')


# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()

# TODO: Calculate subtotal, tax, and total
subtotal = float(price*quantity)
# Tax rate: 9.5%
tax = subtotal*0.095
total = subtotal + tax

# TODO: Round total to 2 dec
total = round(total,2)

# TODO: Print receipt
print("--------------------------")
print(f'Potion of Luck x{quantity} @ ${price} each')
print("--------------------------")
# Print subtotal, tax, and total here
print(f'Subtotal: ${subtotal}')
print(f'Tax: ${tax}')
print(f'Total: ${total}')
print("\nThank you for shopping at\nthe Peculiar Emporium!")#AFTER PASTING YOUR ANSWER YOU MUST REMOVE THE LINE "import s"
#YOUR CODE WILL FAIL IF YOU DO NOT DELETE THE LINE!!!!!!!!!!!!!
