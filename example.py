

class Controller(object):

    def run_account_configuration(self):


        if response == '2':
            self.run_chart_of_accounts()
        pass




    def run_chart_of_accounts(self):
        pass



app = Controller()
app.run_account_configuration()


class Controller(object):

    def __init__(self):
        self.list_of_accounts = [  # Default Chart
            Accounts(acc_num=int(1000), acc_name="Cash", acc_type="Asset"),
            Accounts(acc_num=int(2000), acc_name="Accounts Payable", acc_type="Liability"),
            Accounts(acc_num=int(3000), acc_name="Retained Earnings", acc_type="Equity"),
            Accounts(acc_num=int(4000), acc_name="Sales Revenue", acc_type="Income"),
            Accounts(acc_num=int(5000), acc_name="Cost of Goods Sold", acc_type="Expense"),
            ]

    def run(self):
        user_input = None
        # main loop
        while True:
            if user_input == '1':
                self.show_chart_of_accounts()

    def show_chart_of_accounts(self):
        print("---------------------------------------")
        print("{} - {} - {} - {}".format("Account #", "Account Name", "Account Type", "Account Balance"))
        print("")
        for account in list_of_accounts:
            print("{} - {} - {} - ${}".format(account.acc_num, account.acc_name, account.acc_type, account.acc_balance))
        print("---------------------------------------")



    def add_account_menu(self):
        while True:
            pass


if '__main__' == __name__:
    app = Controller()
    app.run()