from Application_Controller import ApplicationController


class Configuration(object):

    def __init__(self):
        self.chart_of_accounts = ApplicationController()


    def run(self):

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
            self.config_menu()
            print("")
            user_input = input("What would you like to do? ")
            if user_input == "1":
                self.option_one()

            elif user_input == "2":
                self.chart_of_accounts.run()

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


    def config_menu(self):
        print("")
        print("Main Menu:")
        print("1 - Add Personal Account Information")
        print("2 - Chart of Accounts")
        print("3 - Another Option")
        print("4 - Color Scheme")
        print("5 - Finish Account Configuration")

    def option_one(self):

        user_input = None
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


if __name__ == "__main__":
    app = Configuration()
    app.run()