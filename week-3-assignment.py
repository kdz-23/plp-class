
# Week 3 Python assignment 

# A function to calculate the discount of an item
def calculate_discount(price, discount):
    if discount >= 20:
        discountedPrice = (discount / 100) * price # calculate discount if discount is 20% or more
        price = price - discountedPrice
    return price

price = int(input("Enter price: "))
discount = int(input("Enter discount: "))

finalPrice = calculate_discount(price, discount) # Function call
print (f"Final price: {finalPrice}")