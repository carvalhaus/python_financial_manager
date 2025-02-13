from finance_manager.transactions import Transaction

print("===== Personal Finance Manager =====")

print("1. Add Transaction\n"
      "2. View Transactions\n"
      "3. Check Balance\n"
      "4. Save Transactions\n"
      "5. Load Transactions\n"
      "6. Exit\n")

transactions = []
index = 0

while True:
    choice = int(input("Choose an option: "))

    match choice:
        case 1:
            amount = float(input("\nEnter amount: "))
            category = input("Enter category: ")

            transactions.append(Transaction(amount, category))

            print("Transaction added successfully!\n")
            continue
        case 2:
            print("\nThese are yours transactions: ")
            for t in transactions:
                print(t)
            continue
        case 3:
            print("Check")
            continue
        case 4:
            print("Save")
            continue
        case 5:
            print("Load")
            continue
        case 6:
            break


