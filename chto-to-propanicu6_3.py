import random


class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.partners = {}

    def add_partner(self, partner, exposure):
        self.partners[partner] = exposure

    def update_balance(self, loss):
        self.balance -= loss

    def is_bankrupt(self):
        return self.balance < 0

class StressTest:
    def __init__(self, banks, λc, λf, p):
        self.banks = {bank.name: bank for bank in banks}
        self.λc = λc
        self.λf = λf
        self.p = p
        self.bankrupt_banks = []

    def run_test(self, initial_bank):
        print(f"СТАРТУУУЕМ с банка {initial_bank}")
        self.declare_bankruptcy(initial_bank)
        self.contagion()

    def declare_bankruptcy(self, bank_name):
        bank = self.banks[bank_name]
        if bank not in self.bankrupt_banks:
            print(f"{bank.name} теперь банкрот(")
            self.bankrupt_banks.append(bank)
            self.apply_panic(bank)
            self.calculate_losses(bank)

    def apply_panic(self, bankrupt_bank):
        """Применяет панику к партнёрам обанкротившегося банка."""
        for partner in bankrupt_bank.partners.keys():
            if partner not in self.bankrupt_banks:
                panic_loss = bankrupt_bank.partners[partner] * self.p
                partner.update_balance(panic_loss)
                print(f"{partner.name} потерял {panic_loss} из-за паники. Новый баланс: {partner.balance}")

    def calculate_losses(self, bankrupt_bank):
        """Рассчитывает потери партнёров обанкротившегося банка от кредитного и фондового шоков."""
        for partner, exposure in bankrupt_bank.partners.items():
            if partner not in self.bankrupt_banks:
                loss = exposure * (self.λc if partner.is_bankrupt() else self.λf)
                partner.update_balance(loss)
                print(f"{partner.name} потерял {loss} из-за шока. Новый баланс: {partner.balance}")


    def contagion(self):
        """Распространяет банкротства до остановки."""
        new_bankrupts = []
        for bank in self.banks.values():
            if bank.is_bankrupt() and bank not in self.bankrupt_banks:
                new_bankrupts.append(bank)

        if new_bankrupts:
            for bank in new_bankrupts:
                self.declare_bankruptcy(bank.name)
            self.contagion()

# Тестирование с 5 банками, кольцевая и полносвязная структуры
# for a in range(1, 6):

print()
print(f'Test {5}')
print()
bank1 = Bank('Bank1', 1000)
bank2 = Bank('Bank2', 1000)
bank3 = Bank('Bank3', 1000)
bank4 = Bank('Bank4', 1000)
bank5 = Bank('Bank5', 1000)

# Пример для полносвязной структуры
# bank1.add_partner(bank2, 375)
# bank1.add_partner(bank3, 375)
# bank1.add_partner(bank4, 375)
# bank1.add_partner(bank5, 375)
#
# bank2.add_partner(bank1, 375)
# bank2.add_partner(bank3, 375)
# bank2.add_partner(bank4, 375)
# bank2.add_partner(bank5, 375)
#
# bank3.add_partner(bank1, 375)
# bank3.add_partner(bank2, 375)
# bank3.add_partner(bank4, 375)
# bank3.add_partner(bank5, 375)
#
# bank4.add_partner(bank1, 375)
# bank4.add_partner(bank2, 375)
# bank4.add_partner(bank3, 375)
# bank4.add_partner(bank5, 375)
#
# bank5.add_partner(bank1, 375)
# bank5.add_partner(bank2, 375)
# bank5.add_partner(bank3, 375)
# bank5.add_partner(bank4, 375)

bank1.add_partner(bank2, 750)
bank1.add_partner(bank5, 750)

bank2.add_partner(bank1, 750)
bank2.add_partner(bank3, 750)

bank3.add_partner(bank2, 750)
bank3.add_partner(bank4, 750)

bank4.add_partner(bank3, 750)
bank4.add_partner(bank5, 750)

bank5.add_partner(bank1, 750)
bank5.add_partner(bank4, 750)

banks = [bank1, bank2, bank3, bank4, bank5]
λc = 0.3  # random.randint(10, 100) / 100
λf = 0.4  # random.randint(10, 100) / 100
p = 0.5  # random.randint(10, 100) / 100  # Коэффициент паники
print(f'λf = {λf}, λc = {λc}, p = {p}')
stress_test = StressTest(banks, λc, λf, p)
stress_test.run_test(f'Bank{5}')
print()

# for a in range(1, 6):
print()
print(f'Test {5}')
print()
bank1 = Bank('Bank1', 1000)
bank2 = Bank('Bank2', 1000)
bank3 = Bank('Bank3', 1000)
bank4 = Bank('Bank4', 1000)
bank5 = Bank('Bank5', 1000)

#Пример для полносвязной структуры
bank1.add_partner(bank2, 375)
bank1.add_partner(bank3, 375)
bank1.add_partner(bank4, 375)
bank1.add_partner(bank5, 375)

bank2.add_partner(bank1, 375)
bank2.add_partner(bank3, 375)
bank2.add_partner(bank4, 375)
bank2.add_partner(bank5, 375)

bank3.add_partner(bank1, 375)
bank3.add_partner(bank2, 375)
bank3.add_partner(bank4, 375)
bank3.add_partner(bank5, 375)

bank4.add_partner(bank1, 375)
bank4.add_partner(bank2, 375)
bank4.add_partner(bank3, 375)
bank4.add_partner(bank5, 375)

bank5.add_partner(bank1, 375)
bank5.add_partner(bank2, 375)
bank5.add_partner(bank3, 375)
bank5.add_partner(bank4, 375)

# bank1.add_partner(bank2, 750)
# bank1.add_partner(bank5, 750)
#
# bank2.add_partner(bank1, 750)
# bank2.add_partner(bank3, 750)
#
# bank3.add_partner(bank2, 750)
# bank3.add_partner(bank4, 750)
#
# bank4.add_partner(bank3, 750)
# bank4.add_partner(bank5, 750)
#
# bank5.add_partner(bank1, 750)
# bank5.add_partner(bank4, 750)

banks = [bank1, bank2, bank3, bank4, bank5]
λc = 0.6#random.randint(10, 100) / 100
λf = λc#random.randint(10, 100) / 100
p = 0#random.randint(10, 100) / 100  # Коэффициент паники
print(f'λf = {λf}, λc = {λc}, p = {p}')
stress_test = StressTest(banks, λc, λf, p)
stress_test.run_test(f'Bank{5}')
print()
