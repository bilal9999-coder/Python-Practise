inventory = {
    "Laptop": {"price": 1000, "stock": 5},
    "Mouse": {"price": 25, "stock": 10},
    "Keyboard": {"price": 75, "stock": 2}
}

orders = [
    {"customer": "Alice", "item": "Laptop", "quantity": 1},
    {"customer": "Bob", "item": "Mouse", "quantity": 2},
    {"customer": "Alice", "item": "Keyboard", "quantity": 3}, # Note: Only 2 keyboards are in stock!
    {"customer": "Bob", "item": "Laptop", "quantity": 1}
]

Receipt= {}

for things in orders:
    cost = things["customer"]
    item = things["item"]
    quant = things["quantity"]
    if cost in Receipt:
            if(quant<= inventory[item]["stock"]):
                    bill = quant * inventory[item]["price"]
                    Receipt[cost] = Receipt[cost] + bill
                    inventory[item]["stock"] -= quant
            else:
                    bill = inventory[item]["stock"] * inventory[item]["price"]
                    Receipt[cost] = Receipt[cost] + bill
                    inventory[item]["stock"] = 0
    else:
            if(quant<= inventory[item]["stock"]):
                    bill = quant * inventory[item]["price"]
                    Receipt[cost] = bill
                    inventory[item]["stock"] -= quant
            else:
                    bill = inventory[item]["stock"] * inventory[item]["price"]
                    Receipt[cost] = bill
                    inventory[item]["stock"] = 0

print(Receipt,"\n")

for el ,th in inventory.items():
        print(el,": ",th)

# End