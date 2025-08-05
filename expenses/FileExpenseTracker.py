from .tracker import ExpenseTracker
import json
import os
class FileExpenseTracker(ExpenseTracker):
    def __init__(self):
        super().__init__()

    def loadfile(self):
        try:
            with open("data/expenses.json", "r") as file:
                self._ExpenseTracker__expenses = json.load(file)
                print("Expenses loaded successfully.")
        except FileNotFoundError:
            print("No saved file found.")

    def filesave(self):
        try:
            with open("data/expenses.json", "w") as file:
                json.dump(self._ExpenseTracker__expenses, file)
                print("Expenses saved to expenses.json")
        except FileNotFoundError:
            print("Unable to save data")

    def fileremove(self):
        try:
            os.remove("data/expenses.json")
            print("File Deleted Successfully")
        except FileNotFoundError:
            print("No file to delete")
