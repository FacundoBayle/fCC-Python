class Category:

    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        
        return balance

    def transfer(self, amount, budget):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {budget.name}")
            budget.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):    
        if amount <= self.get_balance():
            return True
        else:
            return False

    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for i in self.ledger:
            output += f"{i['description'][:23].ljust(23)}{format(i['amount'], '.2f').rjust(7)}\n"
        output += f"Total: {format(self.get_balance(), '.2f')}"
        
        return output

def create_spend_chart(categories):
    graph = "Percentage spent by category" + "\n"

    category_names = []
    spent = []
    spent_percents = []

    for category in categories: 
        total = 0
        for i in category.ledger:
            if i['amount'] < 0:
                total -= i['amount']
        spent.append(round(total, 2))
        category_names.append(category.name)

    for percents in spent:
        spent_percents.append(round(percents/sum(spent), 2)*100)

    axis = range(100,-10,-10)

    for label in axis: 
        graph += str(label).rjust(3) + "| "
        for percents in spent_percents:
            if percents >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"
                                                
    graph += "    ----" + ("---" * (len(category_names) - 1))
    graph += "\n     "

    len_longest = 0
    
    for names in category_names:
        if len_longest < len(names):
            len_longest = len(names)

    for i in range(len_longest):
        for names in category_names:
            if len(names) > i:
                graph += names[i] + "  "
            else:
                graph += "   "
        if i < len_longest - 1:
            graph += "\n     "

    return graph
