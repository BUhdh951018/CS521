# Game: ATM machine


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

    a_list = []
    for i in range(10):
        a_list.append(Account(id=1, balance=100))
    while True:
        input_id = int(input("Enter an account id:"))
        print()
        if input_id > 10 or input_id < 0:
            print("Please enter a correct id!")
        else:
            while True:
                print('Main menu')
                print('1: check balance')
                print('2: withdraw')
                print('3: deposit')
                print('4: exit')
                num = int(input("Enter a choice:"))

                if num == 1:
                    print("The balance is:", a_list[input_id].getBalance(), "\n")
                elif num == 2:
                    amount = float(input("Enter an amount to withdraw:"))
                    a_list[input_id].withdraw(amount)
                    print()
                elif num == 3:
                    amount = float(input("Enter an amount to deposit:"))
                    a_list[input_id].deposit(amount)
                    print()
                elif num == 4:
                    print()
                    break


if __name__ == '__main__':
    main()
