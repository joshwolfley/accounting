
class AccountInfo(object):

    def __init__(self):
        self.saved_info = 0
        self.company_name = "your company"
        self.user_name = "User"

    def acc_info_menu(self):

        print("1 - view personal information")
        print("2 - Set up Account")
        print("3 - Return to main configuration")

    def run(self):

        while True:
            self.acc_info_menu()

            user_input = input("")

            if user_input == "1":
                if self.saved_info > 0:

                    print(f"Owner name: {self.user_name}")
                    print(f"Company Name: {self.company_name}")
                else:
                    print("Account is not set up yet.")
            elif user_input == "2":
                while user_input != "y":
                    self.user_name = input("What is your name?")

                    print("Your name is \"{}\" correct? Y/N".format(self.user_name))
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

                user_input = None
                while user_input != "y":
                    self.company_name = input("What is the name of your company?")

                    print("The name of your company is \"{}\" correct? Y/N".format(self.company_name))
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
                self.saved_info += 1
            elif user_input == "3":
                break
            else:
                print("Not an option")

