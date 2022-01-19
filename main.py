"""
    1. Из всей библиотеки используется только dt.datetime, можно импортировать только данный модуль
    2.  Для комментирования целой функции лучше использовать Docstrings
    3. В коде используется и f строка и строка через format, желательно делать однообразно
"""
import datetime as dt


class Record:
    # Лучше передать значение None
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        # плохо читаемое условие if not data
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        """
            Record был использован для названия класса, лучше использовать другое название
        """
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                """
                    Можно сократить выражение оператором "+="
                """
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        """
            today и разница в неделю используется несколько раз, можно использовать рассчитанное заранее значение
        """
        today = dt.datetime.now().date()
        for record in self.records:
            """
                Упростить условие возможно с помощью интервального выражения a < b < c
            """
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        """
            Использовать говорящее имя вместо переменно "x"
        """
        x = self.limit - self.get_today_stats()
        """
            1. Использовать круглые скобки для многострочных операторов
            2. Можно использовать 1 return в конце функции, 
        """
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            return('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.
    """
        1. Лишняя передача параметров внутри класса, можно через slef или CashCalculator.USD_RATE
        2. По условию задачи должен принимать только одно значение
    """
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        """
            1. currency_type изменяется сразу после проверки условия
            2. В условиях сравниваешь две разные переменные
            3. Длинные условия, можно короче
        """
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'

        elif currency_type == 'rub':
            """
                 При передачи в функции значения "rub" строка не имеет смысла
             """
            cash_remained == 1.00
            currency_type = 'руб'
        """
            Много return, можно создать сообщение и возвращать одним return
        """
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    """
        Не будет работать, будут проигнорированы все определения текущего класса
    """
    def get_week_stats(self):
        super().get_week_stats()
