class CashRegister:

    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity = 1):
        for i in range(quantity):
            self.items.append(title)

        self.last_transaction = price * quantity
        self.total += price * quantity

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = round(self.total - (self.total * (self.discount / 100)))
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction