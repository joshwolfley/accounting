from Entries import Entry

data = []

tax_rate = .35
beginning_cash_bal = 0
beginning_ar_bal = 0
beginning_inv_bal_sws = 0
beginning_inv_bal_alex = 0
beginning_ap_bal = 0
beginning_retained_earnings = 0


company_name = "Josh Inc."

def total_debs_and_creds():
    total_debits = 0
    total_credits = 0

    for entry in data:

        if entry.type == "DEBIT":
            total_debits += entry.amount
        if entry.type == "CREDIT":
            total_credits += entry.amount

    totaldc = total_debits - total_credits
    return totaldc


def total_sales_rev():
    total_sales_rev = 0

    for entry in data:

        if entry.type == "CREDIT" and entry.account_id == "SALES REV":
            total_sales_rev += entry.amount
        if entry.type == "DEBIT" and entry.account_id == "SALES REV":
            total_sales_rev -= entry.amount
    return total_sales_rev


def total_cogs():
    total_cogs = 0

    for entry in data:

        if entry.type == "DEBIT" and entry.account_id == "COGS":
            total_cogs += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "COGS":
            total_cogs -= entry.amount
    return total_cogs


def total_admin_exp():
    total_admin_exp = 0

    for entry in data:
        if entry.type == "DEBIT" and entry.account_id == "ADMIN EXP":
            total_admin_exp += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "ADMIN EXP":
            total_admin_exp += entry.amount
    return total_admin_exp


def income_taxes():
    gross_margin = total_sales_rev() - total_cogs()
    income_before_taxes = gross_margin - total_admin_exp()
    income_tax_owed = (tax_rate * income_before_taxes)
    return income_tax_owed


def net_income():
    gross_margin = total_sales_rev() - total_cogs()
    income_before_taxes = gross_margin - total_admin_exp()
    net_income = (1 - tax_rate) * income_before_taxes
    return net_income


def print_income_statement():
    gross_margin = total_sales_rev() - total_cogs()
    income_before_taxes = gross_margin - total_admin_exp()

    print("2018 First Quarter Income Statement for {}".format(company_name))
    print("------------------------------")
    print("Sales Revenue:       ${}".format(total_sales_rev()))
    print("Cost of Goods Sold:  ${}".format(total_cogs()))
    print("Gross Margin:        ${}".format(gross_margin))
    print("Admin Expenses:      ${}".format(total_admin_exp()))
    print("Income Before Taxes: ${}".format(income_before_taxes))
    print("Income Taxes:        ${}".format(income_taxes()))
    print("Net Income:          ${}".format(round(net_income(), 2)))
    print("------------------------------")


# Functions for Balance Sheet

def cash():
    change_in_cash = 0

    for entry in data:
        if entry.type == "DEBIT" and entry.account_id == "CASH":
            change_in_cash += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "CASH":
            change_in_cash -= entry.amount

    ending_cash_bal = change_in_cash + beginning_cash_bal
    return ending_cash_bal


def accounts_receivable():
    change_in_ar = 0

    for entry in data:
        if entry.type == "DEBIT" and entry.account_id == "A/R":
            change_in_ar += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "A/R":
            change_in_ar -= entry.amount

    ending_ar_bal = change_in_ar + beginning_ar_bal

    return ending_ar_bal


def inventory_sws():
    change_in_inv_sws = 0

    for entry in data:
        if entry.type == "DEBIT" and entry.account_id == "INV (SWS)":
            change_in_inv_sws += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "INV (SWS)":
            change_in_inv_sws -= entry.amount

    ending_inv_bal_sws = change_in_inv_sws + beginning_inv_bal_sws

    return ending_inv_bal_sws


def inventory_alex():
    change_in_inv_alex = 0

    for entry in data:
        if entry.type == "DEBIT" and entry.account_id == "INV (BOOKS)":
            change_in_inv_alex += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "INV (BOOKS)":
            change_in_inv_alex -= entry.amount

    ending_inv_bal_alex = change_in_inv_alex + beginning_inv_bal_alex

    return ending_inv_bal_alex


def accounts_payable():
    change_in_ap = 0

    for entry in data:
        if entry.type == "CREDIT" and entry.account_id == "A/P":
            change_in_ap += entry.amount
        if entry.type == "DEBIT" and entry.account_id == "A/P":
            change_in_ap -= entry.amount

    ending_ap_bal = change_in_ap + beginning_ap_bal

    return ending_ap_bal


def retained_earnings():
    return beginning_retained_earnings


def print_balance_sheet():
    total_assets = cash() + accounts_receivable() + inventory_sws() + inventory_alex()
    total_liabilities = accounts_payable()
    total_equity = retained_earnings()
    total_liabilities_and_equity = total_liabilities + total_equity
    print("2018 First Quarter Balance Sheet for {}".format(company_name))
    print("Balance Sheet as of March 31, 2018")
    print("------------------------------")
    print("Current Assets")
    print("Cash:                ${}".format(cash()))
    print("A/R:                 ${}".format(accounts_receivable()))
    print("Inventory (SWS):     ${}".format(inventory_sws()))
    print("Inventory (Alex)     ${}".format(inventory_alex()))
    print("Total Assets:        ${}".format(total_assets))
    print("")
    print("Current Liabilities")
    print("Accounts Payable:    ${}".format(accounts_payable()))
    print("")
    print("Owners Equity")
    print("Retained Earnings:   ${}".format(retained_earnings()))
    print("")
    print("liabilities/equity:  ${}".format(total_liabilities_and_equity))
    print("------------------------------")


def print_statement_of_cashflows(): # FIX ME PLZ
    change_in_ar = beginning_ap_bal - accounts_receivable()
    change_in_inv = beginning_inv_bal_alex + beginning_inv_bal_sws - inventory_alex() - inventory_sws()
    change_in_ap = accounts_payable() - beginning_ap_bal
    net_change_in_cash = change_in_ap + change_in_inv + change_in_ar + net_income()
    print("Statement of cash flows for")
    print("2018 First Quarter Statement of Cash Flows for {}".format(company_name))
    print("------------------------------")
    print("Cash Flow From Operating Activities:")
    print("Net Income: {}".format(net_income()))
    print("Adjustments:")
    print("Change in A/R: {}".format(change_in_ar))
    print("Change in Inventory: {}".format(change_in_inv))
    print("Change in A/P: {}".format(change_in_ap))
    print("")
    print("Cash Flow From Investing Activities:")
    print("")
    print("Cash Flow From Financing Activities:")
    print("")
    print("Beginning Cash Balance:               ${}".format(beginning_cash_bal))
    print("Net Change in Cash from the Year:     ${}".format(net_change_in_cash))
    print("Ending Cash Balance:                  ${}".format(cash()))
    #  FIX ME


def display_chart_of_accounts():
    print("current account options:")
    print("")