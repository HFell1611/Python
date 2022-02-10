# Create a Budget class that can instantiate budget objects with balances 
# for different budget categories like food, clothing, and entertainment. 
# These objects should allow for depositing and withdrawing funds from each 
# category, as well computing category balances and transferring balance 
# amounts between categories.

# class Budget():
#     def __init__(self, food, clothing, enter):
#         self.food = food
#         self.clothing = clothing
#         self.enter = enter

class Budget():
    @staticmethod
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

    def transfer(self, category1, category2, amount):
        return