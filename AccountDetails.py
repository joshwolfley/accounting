
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
