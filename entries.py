class Entry(object):

    def __init__(self, type, amount, account, day, month, year, entry_date):
        self.type = type
        self.amount = amount
        self.account_id = account
        self.day = day
        self.month = month
        self.year = year
        self.entry_date = entry_date
