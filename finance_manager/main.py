from finance_manager.transaction_manager import TransactionManager

print("===== Personal Finance Manager =====")

print("1. Add Transaction\n"
      "2. View Transactions\n"
      "3. Check Balance\n"
      "4. Save Transactions\n"
      "5. Load Transactions\n"
      "6. Exit\n")

manager = TransactionManager()

while True:
    try:
        choice = int(input("Choose an option: "))

        if not choice:
            print("❌ Invalid input! Please enter a number.")
            continue

        match choice:
            case 1:
                amount = float(input("\nEnter amount: "))
                category = input("Enter category: ")

                income = input("Is this a income? [Y/N] ").strip().lower()

                if income != "y":
                    amount *= -1

                manager.add_transaction(amount, category)
                continue
            case 2:
                print(manager)
                continue
            case 3:
                manager.check_balance()
                continue
            case 4:
                manager.save_to_file()
                continue
            case 5:
                filename = input("Enter filename where yours transactions are saved (e.g., transactions_2025-02-13.txt): ").strip()
                manager.load_from_file(filename)
                continue
            case 6:
                confirmation = input("Would you like to save your transactions before exit ? [Y/N] ").strip().lower()

                if confirmation == "y":
                    manager.save_to_file()

                print("Exiting program...")
                break
            case _:
                print("❌ Invalid option! Please choose a number between 1 and 6.")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
