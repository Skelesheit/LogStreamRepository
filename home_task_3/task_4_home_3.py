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


"""
1)Напишите класс “кошелек”, у которого есть следующие атрибуты: 
баланс, валюта и имя кошелька. 
Напишите атрибут класса “платежная система”.
 Создайте методы: пополнение баланса, оплата, 
 вывод инфо о количестве средств на балансе
  и удаление счета. 
 Сделайте проверку, что списание с баланса возможно (средств хватает на операцию).

2)*Создайте класс “крипто-кошелек”, наследуемый от класса “кошелек”. 
Создайте в этом классе атрибут “коин”,
 остальные атрибуты должны идти с родительского класса.
  Измените метод информации о средствах на балансе, 
  который покажет количество коинов на балансе. 
  Добавьте метод информации о средствах на балансе в долларах, 
  который переводит коины в доллары. 
  К примеру, можно использовать 2 коина: 
  1 BTC = 72000 USD, 1 ETH = 3500 USD.

Краткая справка и рекомендации:

Атрибут баланса следует сделать защищенным, 
чтобы пользователь знал, что напрямую взаимодействие с балансом не рекомендуется,
 а также при создании экземпляра баланс всегда должен быть равен 0.
  Проверку на вхождение валют в существующие следует сделать внутри метода
   __init_ с помощью конструкции in (“valuta1”, “valuta2”).

*Обращение к атрибутам родительского класса осуществляется через функцию super().
"""
