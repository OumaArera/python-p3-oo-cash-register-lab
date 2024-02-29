class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = [] 

    def add_item(self, title, price, quantity=1):  
        for _ in range(quantity):
          self.items.append(title) 
        self.total += price * quantity  

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print("After the discount, the total comes to ${:.0f}.".format(self.total))  
            return "After the discount, the total is: ${:.2f}".format(self.total)
        else:
            print("There is no discount to apply.")
            return "No discount applied."

    def void_last_transaction(self):
        if self.items:  
            last_transaction = self.items.pop()  
            self.total -= last_transaction[1] * last_transaction[2] 
            # self.total -= last_transaction[1] * last_transaction[2] 
        else:
            return "No transactions to void."


