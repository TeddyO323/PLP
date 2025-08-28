def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to be applied.
    
    Returns:
        float: The final price after applying the discount (if applicable).
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


if __name__ == "__main__":
    try:
        # Prompt user for inputs
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate final price
        final_price = calculate_discount(price, discount_percent)

        # Print result
        if discount_percent >= 20:
            print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
        else:
            print(f"No discount applied. Final price: {final_price:.2f}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")
