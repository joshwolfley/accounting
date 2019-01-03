from accounts import Account
from accountdetail import AccountInfo
from entries import Entry
import datetime
from typing import List
from calculations import Calculations


class PrintStatements(object):

    def __init__(self):
        self.data = []
        self.tax_rate = .35
        self.calculations = Calculations()

    def run(self, account_info, chart_of_accounts):

        self.menu()

        while True:

            user_input = input("Please choose an option")

            if user_input == "1":
                self.option_one(account_info, chart_of_accounts)

            elif user_input == "2":
                self.option_two(account_info, chart_of_accounts)

            elif user_input == "3":
                self.option_three(account_info, chart_of_accounts)

            elif user_input == "4":
                self.option_four(account_info, chart_of_accounts)

            elif user_input == "5":
                pass # Print Statement of Cash Flows

            elif user_input == "6":
                self.option_six()

            elif user_input == "7":
                break
            else:
                self.menu()

    @staticmethod
    def menu():

        print("Main Menu:")
        print("1 - View Chart of Accounts")
        print("2 - Add an Entry")
        print("3 - Print Balance Sheet")
        print("4 - Print Income Statement")
        print("5 - Print Statement of Cash Flows")
        print("6 - View Entries")
        print("7 - Re-configure Account")

    @staticmethod
    def option_one(company_name, chart_of_accounts):

        if chart_of_accounts == []:
            print("")
            print("No Chart of Accounts Available!")
        else:
            print("---------------------------------------")
            print("{} - {} - {} - {}".format("Account #", "Account Name", "Account Type", "Account Balance"))
            print("")
            for account in chart_of_accounts:
                print("{} - {} - {} - ${}".format(account.acc_num, account.acc_name, account.acc_type,
                                                  round(account.acc_balance, 2)))
            print("---------------------------------------")

    def option_two(self, company_name: str, chart_of_accounts: List[Account]) -> int:

        while True:
            print("Debit or Credit? Type \"D\" for Debit or \"C\" for Credit")
            deb_or_cred = input("")
            if deb_or_cred.upper() == "D":
                entry_type = "DEBIT"
            elif deb_or_cred.upper() == "C":
                entry_type = "CREDIT"
            else:
                print("Not an option. Next time follow instructions.")
                break
            print("Which Account does it go in?")
            for account in chart_of_accounts:
                print(f'{account.acc_name}')
            entry_account = input("")
            entry_amount = input("What is the amount?")
            entry_day = input("What is the day of the transaction?")
            entry_month = input("Month?")
            entry_year = input("Year?")

            for account in chart_of_accounts:
                if account.acc_name == entry_account:
                    if account.acc_type == "Asset" or account.acc_type == "Expense":
                        if entry_type == "DEBIT":
                            account.acc_balance += float(entry_amount)
                        elif entry_type == "CREDIT":
                            account.acc_balance -= float(entry_amount)
                    elif account.acc_type == "Liability" or account.acc_type == "Equity" or account.acc_type == "Income":
                        if entry_type == "DEBIT":
                            account.acc_balance -= float(entry_amount)
                        elif entry_type == "CREDIT":
                            account.acc_balance += float(entry_amount)

            print(entry_type)
            print(entry_amount)
            print(entry_account.upper())
            print("{}-{}-{}".format(entry_month, entry_day, entry_year))

            entry_date = datetime.datetime.now()
            self.data.append(Entry(type=entry_type, amount=float(entry_amount), account=entry_account.upper(), day=entry_day,
                              month=entry_month, year=entry_year, entry_date=entry_date.date()))

            entry_diff = self.calculations.total_debs_and_creds((self.data))
            if entry_diff != 0:
                print("Debits and Credits do not equal, add another entry? (The difference is {})".format(entry_diff))
                another_entry = input("Do you want to add more entries? Y/N")
                if another_entry.upper() == "Y":
                    print("")
                elif another_entry.upper() == "N":
                    break
                else:
                    print("Wrong answer")
                    break
            else:
                break

    def option_three(self, company_name, chart_of_accounts):
        print("")
        print("2018 Year End Balance Sheet for {}".format(company_name))
        print("Balance Sheet as of March 31, 2018")
        print("------------------------------")
        print("Assets:")
        for account in chart_of_accounts:
            if account.acc_type == "Asset":
                print(f'{account.acc_name}:   ${round(account.acc_balance, 2)}')
        print("-------------------")
        print("Total Assets:   ${}".format(self.calculations.total_assets(chart_of_accounts)))
        print("")
        print("Liabilities:")
        for account in chart_of_accounts:
            if account.acc_type == "Liability":
                print(f'{account.acc_name}:   ${round(account.acc_balance, 2)}')
        print("")
        print("Equity:")
        for account in chart_of_accounts:
            if account.acc_type == "Equity" and account.acc_name != "Retained Earnings":
                print(f'{account.acc_name}:   ${round(account.acc_balance, 2)}')
        print(f"Retained Earnings:   ${self.calculations.retained_earnings(chart_of_accounts)}")

        print("-------------------")
        print("Total Liabilities and Owners Equity:   ${}".format(self.calculations.total_equity(chart_of_accounts) +
                                                                  self.calculations.total_liabilities(chart_of_accounts)))
        print("------------------------------")
        print("")

    def option_four(self, company_name, chart_of_accounts):

        print("2018 Income Statement for {}".format(company_name))
        print("------------------------------")
        print("Income:")
        for account in chart_of_accounts:
            if account.acc_name == "Sales Revenue":
                print(f'{account.acc_name}:   ${round(account.acc_balance, 2)}')
            elif account.acc_name == "Cost of Goods Sold":
                print(f'{account.acc_name}:   ${round(account.acc_balance, 2)}')
        print(f'Gross Margin:   ${self.calculations.gross_margin(chart_of_accounts)}')
        print("-------------------")
        print("Operating Expenses:")
        for account in chart_of_accounts:
            if account.acc_type == "Expense" and account.acc_name != "Cost of Goods Sold":
                print(f'{account.acc_name}:    ${round(account.acc_balance, 2)}')
        print(f"Income Before Taxes:   ${self.calculations.income_before_taxes(chart_of_accounts)}")
        print("Tax Expense:   ${}".format(self.calculations.tax_expense(chart_of_accounts, self.tax_rate)))
        print("")
        print("Net Income:   ${}".format(self.calculations.net_income(chart_of_accounts, self.tax_rate)))
        print("------------------------------")

    def option_six(self):

        if self.data == []:
            print("No Entries Available!")
        else:
            print("How would you like them Sorted?")
            print("1 - by date entered")
            print("2 - by amount")
            user_input = input("")
            if user_input == "1":
                for entry in self.data:
                    print(
                        " Date: {}-{}-{}  Type: {}  Amount: {}  Account: {}".format(entry.month, entry.day, entry.year,
                                                                                     entry.type,
                                                                                     entry.amount, entry.account_id))
            elif user_input == "2":
                sorted_amount_list = sorted(self.data, key=lambda Entry: Entry.amount, reverse=False)
                for entry in sorted_amount_list:
                    print(" Date: {}-{}-{}  Type: {}  Amount: {}  Account: {}".format(entry.month, entry.day, entry.year, entry.type,
                                                                         entry.amount, entry.account_id))
