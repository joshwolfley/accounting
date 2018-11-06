from Chart_of_Accounts_Controller import ChartOfAccountsApp
from AccountDetails import AccountInfo


class Configuration(object):

    def __init__(self):
        self.chart_of_accounts = ChartOfAccountsApp()
        self.account_info = AccountInfo()

    def run(self):

        print("")
        print("Welcome to Block Ledger! Lets check out {}.".format(self.account_info.company_name))
        print("")
        print("* " * 5)
        print("* $ $ $ *")
        print("* $ $ $ *")
        print("* " * 5)
        print("")
        print("First, let's set up your account.")

        while True:
            self.config_menu()
            print("")
            user_input = input("What would you like to do? ")
            if user_input == "1":
                self.account_info.run()

            elif user_input == "2":
                self.chart_of_accounts.run()

            elif user_input == "3":
                pass  # Do something

            elif user_input == "4":  # add functionality into object
                print("Pick your Color Scheme:")
                print("1 - Arctic")
                print("2 - Savanna")
                print("3 - Night Black")
                color_scheme = input("")
                print("Color Scheme Saved!")

            elif user_input == "5":

                print("Congrats! You have successfully configured {}. Now the fun begins.".format(
                    self.account_info.company_name))
                break

                # Go to actual accounting

            else:
                input("Not an option, try again.")

    def config_menu(self):
        print("")
        print(f"What would you like to do next, {self.account_info.user_name}?")
        print("Main Menu:")
        print("1 - Add Personal Account Information")
        print("2 - Chart of Accounts")
        print("3 - Another Option")
        print("4 - Color Scheme")
        print("5 - Finish Account Configuration")


if __name__ == "__main__":
    app = Configuration()
    app.run()
