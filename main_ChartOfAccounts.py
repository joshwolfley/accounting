from Chart_Of_Accounts import Accounts

list_of_accounts = [  # Default Chart
            Accounts(acc_num=int(1000), acc_name="Cash", acc_type="Asset"),
            Accounts(acc_num=int(2000), acc_name="Accounts Payable", acc_type="Liability"),
            Accounts(acc_num=int(3000), acc_name="Retained Earnings", acc_type="Equity"),
            Accounts(acc_num=int(4000), acc_name="Sales Revenue", acc_type="Income"),
            Accounts(acc_num=int(5000), acc_name="Cost of Goods Sold", acc_type="Expense"),

        ]

def chart_menu():

    print("")
    print("Chart of Accounts Menu: ")
    print("1 - View Current Chart of Accounts")
    print("2 - Add an Account")
    print("3 - Delete an Account")
    print("4 - Update an Account Attribute")
    print("5 - Clear Chart of Accounts")
    print("6 - Return to Default Accounts")
    print("7 - Exit")
    print("")


user_input = "None"

print("")
print("Welcome to the chart of accounts!")
print("What would you like to do?")

while True:
    chart_menu()

    user_input = input("Please choose an option")

    if user_input == "1":
        if list_of_accounts == []:
            print("")
            print("No Chart of Accounts Available!")
        else:
            print("---------------------------------------")
            print("{} - {} - {} - {}".format("Account #", "Account Name", "Account Type", "Account Balance"))
            print("")
            for account in list_of_accounts:
                print("{} - {} - {} - ${}".format(account.acc_num, account.acc_name, account.acc_type,
                                                  account.acc_balance))
            print("---------------------------------------")

    elif user_input == "2":
        while True:
            while True:
                account_num = 0
                try:
                    account_num = int(input("Account Number"))
                except ValueError:
                    print("Account # cannot contain letters")
                    break
                num_in_use = 0
                for account in list_of_accounts:
                    if account.acc_num == account_num:
                        print("Account # already in use. Try again")
                        num_in_use = 1
                if num_in_use == 0:
                    break
            if account_num == 0:
                break
            account_name = input("Account Name")
            account_type = input("Account Type")
            i = 0
            num_of_accounts = len(list_of_accounts)

            while num_of_accounts > i:
                if account_num < list_of_accounts[i].acc_num:
                    list_of_accounts.insert(i, (Accounts(acc_num=int(account_num), acc_name=account_name, acc_type=account_type)))
                    break
                i += 1
            else:
                list_of_accounts.append(Accounts(acc_num=int(account_num), acc_name=account_name, acc_type=account_type))
            add_more = input("Type \"Y\" to enter another account, otherwise click anything else")
            if add_more.upper() != "Y":
                break
    elif user_input == "3":
        removed = 0
        delete_num = 0
        try:
            delete_num = int(input("Which account would you like to delete? Please Enter an Acc #"))
        except ValueError:
            print("Account # cannot contain letters")
        if delete_num != 0:
            for account in list_of_accounts:
                if account.acc_num == delete_num:
                    list_of_accounts.remove(account)
                    print("Account #{} Removed!".format(delete_num))
                    removed = 1
        if removed == 0 and delete_num != 0:
            print("Sorry, there is no account #{}".format(delete_num))
    elif user_input == "4":
        updated = 0
        update_num = 0
        try:
            update_num = int(input("Which account would you like to update? Please Enter an Acc # "))
        except ValueError:
            print("Account # cannot contain letters and must be a whole number greater than 0")
            updated = 1
        for account in list_of_accounts:
            if account.acc_num == update_num:
                print("")
                print("{} - {} - {} - {}".format("Account #", "Account Name", "Account Type", "Account Balance"))
                print("{} - {} - {} - ${}".format(account.acc_num, account.acc_name, account.acc_type, account.acc_balance))
                print("")
                print("What attribute would you like to update for Acc # {}".format(update_num))
                print("1 - Account #")
                print("2 - Account Name")
                print("3 - Account Type")
                print("4 - Account Beginning Balance")
                update = input("")

                if update == "1":
                    new_acc_num = 0
                    duplicate = 0
                    try:
                        new_acc_num = int(input("Please enter new account number: "))
                    except ValueError:
                        print("Account # cannot contain letters and must be a whole number greater than 0")
                        updated = 1
                        break
                    if new_acc_num <= 0:
                        print("Sorry, the account number must be greater than 0")
                        updated = 1
                        break
                    for accounts in list_of_accounts:
                        if accounts.acc_num == new_acc_num:
                            duplicate += 1
                    if duplicate == 1:
                        print("Acc # already taken")
                        updated = 1
                    else:
                        account.acc_num = new_acc_num
                        print("Account # Changed!")
                        sorted_list = sorted(list_of_accounts, key=lambda Accounts: Accounts.acc_num, reverse=False)
                        list_of_accounts = sorted_list
                        updated = 1
                elif update == "2":
                    new_acc_name = input("Please enter new account name: ")
                    account.acc_name = new_acc_name
                    print("Account Name Changed!")
                    updated = 1
                elif update == "3":
                    new_acc_type = input("Please enter new account type: ")
                    account.acc_type = new_acc_type
                    print("Account Type Changed!")
                    updated = 1
                elif update == "4":
                    new_acc_bal = 0.00  # Figure out how to always display 2 decimal places
                    try:
                        new_acc_bal = float(input("Please enter the beginning balance for the account: "))
                    except ValueError:
                        print("Balance cannot contain letters")
                        updated = 1
                        break
                    account.acc_balance = round(new_acc_bal, 2)
                    print("Beginning Balance Updated!")
                    updated = 1
                else:
                    print("Not an option. You're a loser")
                    updated = 1
        if updated == 0:
            print("Not a valid acc #")
    elif user_input == "5":
        delete_all = input("Are you sure you want to delete your chart of accounts? Type \"Y\" to proceed ")
        if delete_all.upper() == "Y":
            list_of_accounts = []
            print("Chart of Accounts Deleted!")
        else:
            print("Chart of accounts not deleted.")
    elif user_input == "6":
        list_of_accounts = [  # Default Chart
            Accounts(acc_num=int(1000), acc_name="Cash", acc_type="Asset"),
            Accounts(acc_num=int(2000), acc_name="Accounts Payable", acc_type="Liability"),
            Accounts(acc_num=int(3000), acc_name="Retained Earnings", acc_type="Equity"),
            Accounts(acc_num=int(4000), acc_name="Sales Revenue", acc_type="Income"),
            Accounts(acc_num=int(5000), acc_name="Cost of Goods Sold", acc_type="Expense"),
        ]
        print("Default Chart of accounts has been restored.")
    elif user_input == "7":
        break
    else:
        print("Not an option. Here are the available options:")
