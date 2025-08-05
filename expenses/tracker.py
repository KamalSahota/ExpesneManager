class ExpenseTracker:
    def __init__(self):
        self.__expenses={}
        pass

    def welcome(self):
        print("Welcome to Kamal's Expense Tracker!")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Show summary (total, average, max, min)")
        print("4. Remove an Expense.")
        print("5. To Load File.")
        print("6. To Save File")
        print("7. To remove File Data.")
        print("8. exit")

    def add_expense(self,name,amount):
        self.__expenses[name]=amount

    def remove_expense(self,name):
        if name in self.__expenses:
            del self.__expenses[name]
            return(f"Deleted Successfully.")

    def get_summary(self):
        total = sum(self.__expenses.values())
        avg = total / len(self.__expenses) if self.__expenses else 0
        max_price = max(self.__expenses.values())
        min_price = min(self.__expenses.values())
        for name,price in self.__expenses.items():
            if price == max_price:
                max_item = name
            if price == min_price:
                min_item = name
        return (f"Total is: {total} Average is: {avg} \nMost Expensive is: {max_item} - {max_price} Least Expensive is: {min_item} - {min_price}")
        
    
    def get_expenses(self):
        return self.__expenses.copy()