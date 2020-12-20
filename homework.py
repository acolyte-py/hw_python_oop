import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        day_spent = 0
        date_today = dt.datetime.today().date()
        for i in self.records:
            if i.date == date_today:
                day_spent += i.amount
        return day_spent

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.today().date()
        delta = dt.timedelta(days=7)
        date_week_ago = today - delta
        for i in self.records:
            if date_week_ago < i.date <= today:
                week_stats += i.amount
        return week_stats


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = date
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()


class CashCalculator(Calculator):

    USD_RATE = 73.11
    EURO_RATE = 88.34

    def get_today_cash_remained(self, currency):
        currency_dict = {
            "rub": (1, "руб"),
            "usd": (self.USD_RATE, "USD"),
            "eur": (self.EURO_RATE, "Euro")
        }
        if currency in currency_dict:
            rate = currency_dict[currency][0]
            name = currency_dict[currency][1]
        else:
            return f'Не знаю такую валюту'
        if self.limit > self.get_today_stats():
            cash_remained = round(self.limit / rate
                                  - self.get_today_stats() / rate, 2)
            return f'На сегодня осталось {cash_remained} {name}'
        elif self.limit / rate == self.get_today_stats() / rate:
            return 'Денег нет, держись'
        else:
            cash_remained = abs(round(self.limit / rate
                                - self.get_today_stats() / rate, 2))
            return f'Денег нет, держись: твой долг - {cash_remained} {name}'


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        remain = self.limit - self.get_today_stats()
        if remain <= 0:
            return 'Хватит есть!'
        else:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {remain} кКал')
