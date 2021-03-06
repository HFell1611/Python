class Budget():
    @staticmethod
    def move(budget1, category1, budget2, category2, amount):
        if budget1.withdraw(category1, amount):
            budget2.deposit(category2, amount)
    
    def __init__(self, **balances):
        self.cats = balances
        for cat in balances:
            setattr(self, cat, balances[cat])
        self.total = sum(balances.values())
    
    def deposit(self, category, amount):
        self.total += amount
        if category.lower() in self.cats:
            self.cats[category.lower()] += amount
        else:
            self.cats[category.lower()] = amount
        setattr(self, category.lower(), self.cats[category.lower()])
        print(f"{category.capitalize()} budget is now {self.cats[category.lower()]}")

    def withdraw(self, category, amount):
        if getattr(self, category.lower()) >= amount:
            self.total -= amount
            self.cats[category.lower()] -= amount
            setattr(self, category.lower(), self.cats[category.lower()])
            print(f"{category.capitalize()} budget is now {self.cats[category.lower()]}")
        else:
            print("Insufficient funds for category:", category)
        return getattr(self, category.lower()) >= amount
    
    def transfer(self, category1, category2, amount):
        if self.withdraw(category1, amount):
            self.deposit(category2, amount)
            print(f"Transferred {amount} from {category1.capitalize()} to {category2.capitalize()}")
    
    def __str__(self):
        newline = '\n'
        return f"""-----\nTotal budget is {self.total}.\n{newline.join([f"{cat.capitalize()}: {self.cats[cat] / self.total * 100:.2f}%" for cat in self.cats])}\n-----"""

# Example usage
budget = Budget(food=100, clothing=50, entertainment=100, utilities=200, rent=300)
print(budget.rent)
budget.deposit("Entertainment", 20)
budget.withdraw("rent", 50)
budget.transfer("entertainment", "rent", 50)
print(budget)
newbudget = Budget(food=50, clothing=30, entertainment=20, utilities=100, rent=200)
Budget.move(budget, "rent", newbudget, "food", 30)
print(newbudget)