from enum import StrEnum, IntEnum


class Currency(StrEnum):
    Rubles = "RUB"
    Dollars = "USD"
    Euro = "EUR"
    Tenge = "TENGE"


class PayMentSystem(StrEnum):
    Visa = "Visa"
    Mastercard = "Mastercard"
    MIR = "MIR"


class Coin(IntEnum):
    BTC = 72000
    ETH = 3500


class Wallet:

    def __init__(self, name: str,
                 currency: Currency,
                 payment_system: PayMentSystem):
        self.name = name
        self._balance = 0
        self.currency = currency
        self.payment_system = payment_system

    def pay(self, amount: float):
        if amount < 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self._balance:
            raise ValueError("сумма списания должна быть меньше баланса")
        self._balance -= amount

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    def info(self):
        print(self)

    def __str__(self):
        return f"Кошелёк {self.name} : {self._balance} {self.currency}"

    def delete_account(self):
        self._balance = 0


class CryptoWallet(Wallet):
    def __init__(self, name: str, currency: Currency,
                 payment_system: PayMentSystem, coin: Coin):
        super().__init__(name, currency, payment_system)
        self.type_coin = coin

    def transfer_to_dollars(self):
        return self._balance * self.type_coin

    def info_in_dollars(self):
        print(f"Баланс долларов в кошельке: {self.transfer_to_dollars()}")

    def __str__(self):
        return f"Крипто Кошелёк {self.name} : {self._balance} {self.type_coin}"
