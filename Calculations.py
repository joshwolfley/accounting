from Account import Account
from AccountDetails import AccountInfo
from Entries import Entry


class Calculations(object):

    def __init__(self):
        self.data = []

    def run(self, account_info, chart_of_accounts):

        self.menu()

        while True:

            user_input = input("Please choose an option")

            if user_input == "1":
                self.option_one(account_info, chart_of_accounts)

            elif user_input == "2":
                self.option_two()

            elif user_input == "3":
                pass

            elif user_input == "4":
                pass

            elif user_input == "5":
                pass

            elif user_input == "6":
                self.option_six()

            elif user_input == "7":
                break
            else:
                self.menu()

    def menu(self):

        print("Main Menu:")
        print("1 - View Chart of Accounts")
        print("2 - Add an Entry")
        print("3 - Print Balance Sheet")
        print("4 - Print Income Statement")
        print("5 - Print Statement of Cash Flows")
        print("6 - View Entries")
        print("7 - Re-configure Account")

    def option_one(self, account_info, chart_of_accounts):

        for account in chart_of_accounts:
            if chart_of_accounts == []:
                print("")
                print("No Chart of Accounts Available!")
            else:
                print("---------------------------------------")
                print("{} - {} - {} - {}".format("Account #", "Account Name", "Account Type", "Account Balance"))
                print("")
                for account in chart_of_accounts:
                    print("{} - {} - {} - ${}".format(account.acc_num, account.acc_name, account.acc_type,
                                                      account.acc_balance))
                print("---------------------------------------")
            print(account.acc_num)
    def option_two(self):

        while True:
            total_debs = 0
            total_creds = 0
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

            self.data.append(Entry(type=entry_type, amount=float(entry_amount), account=entry_account.upper(), day=entry_day,
                              month=entry_month, year=entry_year))

            for entry in self.data: # Do debits and credits equal?
                if entry.type == "DEBIT":
                    total_debs += entry.amount
                else:
                    total_creds += entry.amount
            entry_diff = total_debs - total_creds

            if total_creds != total_debs:
                print("Debits and Credits do not equal, add another entry? (The difference is {})".format(entry_diff))
                another_entry = input("Do you want to add more entries? Y/N")
                if another_entry.upper() == "Y":
                    print("")
                elif another_entry.upper() == "N":
                    break
            break
    def option_six(self):
        if self.data == []:
            print("No Entries Available!")
        else:
            for entry in self.data:
                print(" Date: {}-{}-{}  Type: {}  Amount: {}  Account: {} ".format(entry.month, entry.day, entry.year, entry.type,
                                                                         entry.amount, entry.account_id))
