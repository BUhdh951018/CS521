# The Account class


class Account:

    def __init__(self, id=0, balance=100.0, annualInterestRate=0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 1200

    def getMonthlyInterest(self):
        return self.getAnnualInterestRate() * self.__balance

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount


def main():
    account = Account(1122, 20000, 4.5)
    account.withdraw(2500)
    account.deposit(3000)
    print("The account id: {0:4}".format(account.getId()))
    print("The account balance: {0:5}".format(account.getBalance()))
    print("The account monthly interest rate: {0:4.5f}".format(account.getMonthlyInterestRate()))
    print("The account monthly interest: {0:6.2f}".format(account.getMonthlyInterest()))


if __name__ == '__main__':
    main()

