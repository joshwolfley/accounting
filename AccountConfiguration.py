from Chart_Of_Accounts import Accounts


def config_menu():
    print("")
    print("Main Menu:")
    print("1 - Add Personal Account Information")
    print("2 - Chart of Accounts")
    print("3 - Another Option")
    print("4 - Color Scheme")
    print("5 - Finish Account Configuration")


def print_chart_of_accounts():
    print("---------------------------------------")
    print("{} - {} - {} - {}".format("Account #", "Account Name", "Account Type", "Account Balance"))
    print("")
    for account in list_of_accounts:
        print("{} - {} - {} - ${}".format(account.acc_num, account.acc_name, account.acc_type,
                                          account.acc_balance))
    print("---------------------------------------")


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


list_of_accounts = [  # Default Chart
            Accounts(acc_num=int(1000), acc_name="Cash", acc_type="Asset"),
            Accounts(acc_num=int(2000), acc_name="Accounts Payable", acc_type="Liability"),
            Accounts(acc_num=int(3000), acc_name="Retained Earnings", acc_type="Equity"),
            Accounts(acc_num=int(4000), acc_name="Sales Revenue", acc_type="Income"),
            Accounts(acc_num=int(5000), acc_name="Cost of Goods Sold", acc_type="Expense"),

        ]

print("")
print("Welcome to Block Ledger!")
print("")
print("* " * 5)
print("* $ $ $ *")
print("* $ $ $ *")
print("* " * 5)
print("")
print("Let's set up your account.")


while True:
    config_menu()
    print("")
    user_input = input("What would you like to do? ")
    if user_input == "1":
        user_input = "nothing"
        while user_input != "y":
            user_name = input("What is your name?")

            print("\"{}\" correct? Y/N".format(user_name))
            user_input = input()
            if user_input.upper() == "Y":
                print("Name Saved")
            elif user_input.upper() == "N":
                print("")
            else:
                while user_input.upper() != "Y":
                    print("Not an option. Please type \"Y\" for yes and \"N\" for no")
                    user_input = input()
                    if user_input.upper() == "Y":
                        print("Name Saved")
                        break
                    elif user_input.upper() == "N":
                        break

        user_input = "nothing"
        while user_input != "y":
            company_name = input("What is the name of your company?")

            print("\"{}\" correct? Y/N".format(company_name))
            user_input = input()
            if user_input.upper() == "Y":
                print("Name Saved")
            elif user_input.upper() == "N":
                print("")
            else:
                while user_input.upper() != "Y":
                    print("Not an option. Please type \"Y\" for yes and \"N\" for no")
                    user_input = input()
                    if user_input.upper() == "Y":
                        print("Name Saved")
                        break
                    elif user_input.upper() == "N":
                        break
        print("Account information stored!")

    elif user_input == "2":
        pass  # Link to chart of accounts

    elif user_input == "3":
        pass  # Do something

    elif user_input == "4":
        print("Pick your Color Scheme:")
        print("1 - Arctic")
        print("2 - Savanna")
        print("3 - Night Black")
        color_scheme = input("")
        print("Color Scheme Saved!")

    elif user_input == "5":
        break  # Finish

    else:
        input("Not an option, try again.")

print("Congrats! You have successfully configured your account. Now the fun begins. ")


