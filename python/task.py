product_prices = {"Product A": 20, "Product B": 40, "Product C": 50}
gift_wrap_fee = 1
shipping_fee = 5

def calculate_totals(product_quantities):
    subtotal = 0
    products = {}
    
    for name, qty in product_quantities.items():
        price = product_prices[name]
        products[name] = {"quantity": qty, "amount": qty * price}
        subtotal += products[name]["amount"]
        
    return products, subtotal

def calculate_discounts(products, subtotal):
    discount_name = ""
    discount_amount = 0
    
    if subtotal > 200:
        discount_name = "flat_10_discount" 
        discount_amount = 10
    else:
        for name, product in products.items():
            if product["quantity"] > 10:
                discount_name = "bulk_5_discount"
                discount_amount = round(product["amount"] * 0.05)
                break
                
        if sum(p["quantity"] for p in products.values()) > 20:
            new_discount = round(subtotal * 0.1)
            if new_discount > discount_amount:
                discount_name = "bulk_10_discount"
                discount_amount = new_discount
        
    return discount_name, discount_amount
    
def calculate_fees(products):
    gift_wrap_qty = 0
    for name, product in products.items():
        gift_wrap = input(f"Gift wrap {product['quantity']} units of {name}? (y/n) ")
        if gift_wrap == "y":
            gift_wrap_qty += product["quantity"]
    
    shipping_pkg = (sum(p["quantity"] for p in products.values()) + 9) // 10
    
    return gift_wrap_qty * gift_wrap_fee, shipping_pkg * shipping_fee
    
if __name__ == "__main__":
    product_quantities = {}
    for name in product_prices:
        qty = int(input(f"Enter quantity for {name}: "))
        product_quantities[name] = qty
        
    products, subtotal = calculate_totals(product_quantities)  
    discount_name, discount_amount = calculate_discounts(products, subtotal)
    gift_wrap_fee, shipping_fee = calculate_fees(products)
    
    print()
    for name, product in products.items():
        print(f"{name}: {product['quantity']} units, ${product['amount']}")
        
    print(f"Subtotal: ${subtotal}")
    
    if discount_amount > 0:
        print(f"Discount ({discount_name}): -${discount_amount}")
        
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    
    total = subtotal - discount_amount + shipping_fee + gift_wrap_fee
    print(f"Total: ${total}")
