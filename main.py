from expenses.tracker import ExpenseTracker
from expenses.FileExpenseTracker import FileExpenseTracker

tracker=FileExpenseTracker()

while True:
    tracker.welcome()
    choice=int(input("Please input your Choice: "))
    
    if(choice==1):
        expenses=tracker.get_expenses()
        numofitems=int(input("Please tell me number of items: "))
        #variable yes is defined to skip duplicates
        yes="y"
        #Here's the main code starts that will store items     
        for i in range(numofitems):
            name=input("Please Enter the item name: ")
            #Here it checks for name whether it exists or not
            #and will replace it when y is given as input
            if name in expenses:
                replace=input("Item already exists replace it with new one then press Y. ")
                if(replace!=yes):
                    print("skipped")
                    continue
            #programme continues if no duplicate is found
            price=int(input("Please Enter the items price: "))
            #here its storing values to expenses
            tracker.add_expense(name,price)
                #expense_names.append(name)
                #expense_amounts.append(price)
            print("")

    elif(choice==2):
        expenses=tracker.get_expenses()
        for item, price in expenses.items():
            #print(item, "-", price)
            print(f"{item} - {price}")

    elif(choice==3):
        summary=tracker.get_summary()
        print(summary)

    elif(choice==4):
        expenses=tracker.get_expenses()
        if not expenses:
            print("No Expenses to remove") 
            tracker.welcome()
        name=input("Please Enter the name of item to be removed: ")
        if name in expenses:
            deletion=tracker.remove_expense()
            print(deletion)
        else:
            print("No item to be deleted.")
        
    elif(choice==5):
        tracker.loadfile()
    elif(choice==6):
        tracker.filesave()
    elif(choice==7):
        tracker.fileremove()
    else:
        print("Bye")
        break