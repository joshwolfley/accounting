from Financials import print_balance_sheet
from Financials import print_income_statement
from Financials import print_statement_of_cashflows
from Financials import data
from Entries import Entry


def menu():
    print("Main Menu:")
    print("1 - menu")
    print("2 - Add an Entry")
    print("3 - Print Balance Sheet")
    print("4 - Print Income Statement")
    print("5 - Print Statement of Cash Flows")
    print("6 - View Entries")
    print("7 - Exit")


menu()
while True:
    user_option = input("what would you like to do now?")
    if user_option == "1":
        menu()
    elif user_option == "2":
        while True:
            entry_type = "DEBIT"
            print("Debit or Credit? Type \"D\" for Debit or \"C\" for Credit")
            deb_or_cred = input("")
            if deb_or_cred.upper() == "D":
                entry_type = "DEBIT"
            elif deb_or_cred.upper() == "C":
                entry_type = "CREDIT"
            else:
                print("Not an option. Next time follow instructions.")
                break
            entry_account = input("What account does it go in to?")
            entry_amount = input("What is the amount?")
            entry_day = input("What is the day of the transaction?")
            entry_month = input("Month?")
            entry_year = input("Year?")

            print(entry_type)
            print(entry_amount)
            print(entry_account.upper())
            print("{}-{}-{}".format(entry_month, entry_day, entry_year))

            data.append(Entry(type=entry_type, amount=float(entry_amount), account=entry_account.upper(), day=entry_day, month = entry_month, year = entry_year))

            another_entry = input("Do you want to add more entries? Y/N")
            if another_entry.upper() == "Y":
                print("")
            elif another_entry.upper() == "N":
                break

    elif user_option == "3":
        print_balance_sheet()
    elif user_option == "4":
        print_income_statement()
    elif user_option == "5":
        print_statement_of_cashflows()
    elif user_option == "6":
        if data == []:
            print("No Entries Available!")
        else:
            for entry in data:
                print(" Date: {}-{}-{}  Type: {}  Amount: {}  Account: {} ".format(entry.month, entry.day, entry.year, entry.type, entry.amount, entry.account_id))
    elif user_option == "7":
        break
    else:
        print("Not an option...")
        menu()

