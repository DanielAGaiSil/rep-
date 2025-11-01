#Personal Finance Tracker
#- Add income/expenses with categories
#- View spending breakdown by category
#- Save/load transaction history
#- Monthly budget alerts

import json
from datetime import datetime

DATA_FILE = "finance_data.json"

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"transactions": []}  #Start without a budget

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def set_budget(data):
    print("\n💰 Set Monthly Budget")
    while True:
        try:
            budget = float(input("Enter your monthly budget: $"))
            if budget <= 0:
                print("❌ Budget must be greater than $0")
                continue
            data["budget"] = budget
            save_data(data)
            print(f"✅ Budget set to ${budget:.2f}")
            break
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")

def add_transaction(data):
    print("\n➕ Add Transaction")
    while True:
        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                print("❌ Amount must be greater than $0")
                continue
            break
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")
    
    category = input("Category (e.g., Food, Rent, Entertainment): ").title()
    note = input("Note (optional): ")
    
    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "amount": amount,
        "category": category,
        "note": note
    }
    
    data["transactions"].append(transaction)
    save_data(data)
    print("✅ Transaction added!")

def view_spending(data):
    print("\n📊 Spending Summary")
    
    #Calculate totals
    categories = {}
    total = 0
    for t in data["transactions"]:
        category = t["category"]
        amount = t["amount"]
        categories[category] = categories.get(category, 0) + amount
        total += amount
    
    #Show category breakdown
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")
    
    #Budget status
    if "budget" in data:
        remaining = data["budget"] - total
        print(f"\nTotal: ${total:.2f} | Budget: ${data['budget']:.2f}")
        if remaining < 0:
            print(f"⚠️ You're ${abs(remaining):.2f} OVER budget!")
        else:
            print(f"✅ ${remaining:.2f} remaining in budget")
    else:
        print(f"\nTotal spending: ${total:.2f} (No budget set - use option 3 to set one)")

#Where the program actually works
def main():
    data = load_data()
    
    while True:
        print("\n💵 Personal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Spending Summary")
        print("3. Set Monthly Budget")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_transaction(data)
        elif choice == "2":
            view_spending(data)
        elif choice == "3":
            set_budget(data)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()