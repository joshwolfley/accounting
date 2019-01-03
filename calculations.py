from typing import List


class Calculations(object):

    # Balance Sheet Calculations

    def total_debs_and_creds(self, data):
        total_debs = 0
        total_creds = 0
        for entry in data:  # Do debits and credits equal?
            if entry.type == "DEBIT":
                total_debs += entry.amount
            else:
                total_creds += entry.amount
        entry_diff = total_debs - total_creds
        return round(entry_diff, 2)

    def total_assets(self, chart_of_accounts):
        total_assets = 0
        for account in chart_of_accounts:
            if account.acc_type == "Asset":
                total_assets += account.acc_balance
        return round(total_assets, 2)

    def total_liabilities(self, chart_of_accounts):
        total_liabilities = 0
        for account in chart_of_accounts:
            if account.acc_type == "Liability":
                total_liabilities += account.acc_balance
        return round(total_liabilities, 2)

    def total_equity(self, chart_of_accounts):
        total_equity = 0
        for account in chart_of_accounts:
            if account.acc_type == "Equity":
                total_equity += account.acc_balance
        return total_equity + self.income_before_taxes(chart_of_accounts)

    def retained_earnings(self, chart_of_accounts):
        retained_earnings = 0
        for account in chart_of_accounts:
            if account.acc_name == "Retained Earnings":
                retained_earnings = account.acc_balance
        return retained_earnings + self.income_before_taxes(chart_of_accounts)

    # Income Statement Calculations

    def gross_margin(self, chart_of_accounts):
        gross_margin = 0
        for account in chart_of_accounts:
            if account.acc_name == "Sales Revenue":
                gross_margin += account.acc_balance
            elif account.acc_name == "Cost of Goods Sold":
                gross_margin -= account.acc_balance
        return round(gross_margin, 2)

    def income_before_taxes(self, chart_of_accounts):
        income_before_taxes = 0
        for account in chart_of_accounts:
            if account.acc_type == "Income":
                income_before_taxes += account.acc_balance
            elif account.acc_type == "Expense":
                income_before_taxes -= account.acc_balance
        return round(income_before_taxes, 2)

    def tax_expense(self, chart_of_accounts, tax_rate):
        return round(self.income_before_taxes(chart_of_accounts) * tax_rate, 2)

    def net_income(self, chart_of_accounts, tax_rate):
        return round(self.income_before_taxes(chart_of_accounts) * (1-tax_rate), 2)
