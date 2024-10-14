class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

class Bill:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        item = GroceryItem(name, price, quantity)
        self.items.append(item)

    def generate_bill(self):
        total = 0
        print("\n==== BILL ====")
        for item in self.items:
            item_total = item.get_total_price()
            print(f"{item.name} - {item.quantity} @ {item.price} = {item_total}")
            total += item_total
        print(f"Total: {total}")
        print("===============")

# Example Usage
bill = Bill()

bill.add_item("Apple", 2, 5)
bill.add_item("Banana", 1, 6)
bill.add_item("Orange", 3, 4)

bill.generate_bill()
