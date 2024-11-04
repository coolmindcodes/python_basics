class Account:
    def __init__(self, full_name, acc_num, phone, balance): #method/function constructor --> set up info
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited successfully to account {self.acc_num}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds. Balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully from account {self.acc_num}")

    def check_balance(self):
        print(f"Balance for account {self.acc_num} is: {self.balance}")


# data and methods manipulate the data
kevo_acc = Account("Kevin Maina", "0001", "0712222333", 1000)
sara_acc = Account("Sarah Hassan", "002", "0723432234", 1800)
willy_account = Account(balance=8000, acc_num="003", full_name="Will Jones", phone="0744556677")
kevo_acc.deposit(2000)
kevo_acc.check_balance()
kevo_acc.withdraw(500)
kevo_acc.check_balance()

sara_acc.deposit(1000)
sara_acc.check_balance()
