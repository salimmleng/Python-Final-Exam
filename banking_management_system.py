

from abc import ABC
import random
class User(ABC):
    def __init__(self,name,email,address,account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type    

class Grahok(User):

    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address, account_type)
        self.history = []
        self.loan_count = 0
        
    
    def deposite(self,account_number,amount,bank):
        bank.total_balance += amount
        bank.users[account_number]['account_balance'] += amount
        bank.users[account_number]['transaction_history'].append(f'Deposited {amount} to {account_number} number')
        
        print('Deposited successfully')
    

    def withdraw(self,account_number,amount,bank):
        if bank.users[account_number]['account_balance'] == 0:
            print('Bank is bankrupt')

        elif amount > bank.users[account_number]['account_balance']:
            print('Withdrawal amount exceeded')

        else:
            bank.total_balance -= amount
            bank.users[account_number]['transaction_history'].append(f'Withdrawl {amount} from {account_number} number')
            bank.users[account_number]['account_balance'] -= amount
            print('Withdraw successful')


    def check_balance(self,account_number,bank):
        print(bank.users[account_number]['account_balance'])


    def take_loan(self,account_number,amount,bank):
        if bank.loan_system:
            if account_number in bank.users:
                if self.loan_count >= 2:
                      print('Loan is not applicable more than two times ')
                      return
        
                bank.total_balance -= amount
                bank.users[account_number]['account_balance'] += amount
                bank.users[account_number]['transaction_history'].append(f'Loan:  {amount} taka')
                bank.total_loan += amount
                self.loan_count += 1
                print(f'Loan {amount} got successfully')
            else:
                print('Account number is not exist')
        else:
            print('Loan system is disabled now')



    def transfer_money(self,from_account,to_account,amount,bank):
        if to_account not in bank.users or from_account not in bank.users:
            print('Account does not exist')
            return
        if bank.users[from_account]['account_balance'] < amount:
            print('Transfer is not possible')
            return
        
        bank.users[from_account]['account_balance'] -= amount
        bank.users[to_account]['account_balance'] += amount
        bank.users[from_account]['transaction_history'].append(f'Transferred to {amount} {to_account}')
        bank.users[to_account]['transaction_history'].append(f'Received {amount} from {from_account}')
        print(f'Transferred {amount} succeessfully')


    def transaction_history(self,account_number,bank):
        print('Transaction history below')
        print(bank.users[account_number]['transaction_history'])


class Bank:

    def __init__(self, name):
        self.name = name
        self.total_balance = 0
        self.total_loan = 0
        self.loan_system = False
        self.users = {}
        self.admin_list = []
        self.__account_number = self.__generate_account_number()
    
    def create_user_account(self,name,email,address,account_type):
        account_number = random.randint(10000,99999)

        if account_number == self.__account_number:
            account_number = random.randint(10000,99999)
        else:
            self.__account_number = account_number
            self.users[account_number] = {
                'name' : name,
                'email': email,
                'address' : address,
                'account_type' : account_type,
                'account_balance': 0,
                'transaction_history': [] 
            }
            print(f'Account created successfully Name: {name}\tAccount_type: {account_type}\t Account number: {account_number}')
    
    def create_admin_account(self,name,email,address,account_type):
        account = (name,email,address,account_type)
        self.admin_list.append(account)
        print('Admin account created successfully')
        print('You are now admin in the bank')

    def __generate_account_number(self):
        return random.randint(10000,99999) 
        
    def available_balance(self):
        print(self.total_balance)

    def loan_amount(self):
        print(self.total_loan)

    def show_user_list(self):
        print('All user account lists')
        for account_number,user in self.users.items():
            print(f"Account Number: {account_number}, Name: {user['name']}")

    

    
class Admin(User):

    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address, account_type)
     
   

    def check_total_balance(self, bank):
        return bank.available_balance()
        
    def check_total_loan(self, bank):
        return bank.loan_amount()
    
    def delete_account(self,account_number,bank):
        if account_number in bank.users:
            del bank.users[account_number]
            print('Account number deleted')
        else:
            print('Account number not exist')

    
    def show_user_list(self,bank):
        return bank.show_user_list()
    
    def loan_system(self,status,bank):
        if status == 'on':
            bank.loan_system = True
            print('Loan system enabled')

        else:
            bank.loan_system = False
            print('Loan system disabled')

    
bank = Bank('My bank')
gr = Grahok('salim','salim@gmail','Dhaka','current')
admin = Admin('salim','salim@gmail','Dhaka','current')

while True:

    print('Options')
    print('1: User')
    print('2: Admin')
    print('3: Exit')

    ch = int(input("Enter your choice: "))

    if ch == 1:
       while True:
            print('------------##------------')
            print('Dear Grahok, Welcome to Banking management system')
            print('Options')
            print('1: Create account')
            print('2: Deposite')
            print('3: Withdraw')
            print('4: Check balance')
            print('5: Transaction history')
            print('6: Take loan')
            print('7: Transfer money')
            print('8: Exit')

            ch = int(input("Enter your choice: "))

            if ch == 1:
               name = input("Enter your name: ")
               email = input("Enter your email: ")
               address = input("Enter your address: ")
               account_type = input("Enter account type: ")
               bank.create_user_account(name,email,address,account_type)
            

            elif ch == 2:
               acc_num = int(input("Enter acc number: "))
               dep = int(input("Enter deposite money: "))
               gr.deposite(acc_num,dep,bank)
            elif ch == 3:
               acc_num = int(input("Enter acc number: "))
               withd  = int(input('Enter withdrw money: '))
               gr.withdraw(acc_num,withd,bank)

            elif ch == 4:
               acc_num = int(input("Enter acc number: "))
               gr.check_balance(acc_num,bank)

            elif ch == 5:
               acc_num = int(input("Enter acc number: "))
               gr.transaction_history(acc_num,bank)
    
            elif ch == 6:
              acc_num = int(input("Enter account number: "))
              loan = int(input('Enter loan amount: '))
              gr.take_loan(acc_num,loan,bank)

            elif ch == 7:
              fro_account = int(input("From account: "))
              t_account = int(input("To account : "))
              taka = int(input("Enter amount: "))
              gr.transfer_money(fro_account,t_account,taka,bank)

            elif ch == 8:
              break

            else:
               print('Invalid input')


    elif ch == 2:

        while True:
            print('Options')
            print(' 1 : Create account')
            print(' 2 : Delete account')
            print(' 3 : Show user list')
            print(' 4 : Total Bank balance')
            print(' 5 : Total loan amount')
            print(' 6 : Set loan system')
            print(' 7 : Exit')

            ch = int(input("Enter your choice: "))

            if ch == 1:
                name = input("Enter your name: ")
                email = input("Enter your gmail: ")
                address = input("Enter your address: ")
                account_type = input("Enter account type: ")
                bank.create_admin_account(name,email,address,account_type)

            elif ch == 2:
                acc_num = int(input("Enter account number: "))
                admin.delete_account(acc_num,bank)

            elif ch == 3:
               
                admin.show_user_list(bank)

            elif ch == 4:
                admin.check_total_balance(bank)
            
            elif ch == 5:
                admin.check_total_loan(bank)

            elif ch == 6:
                status = input("Turn loan system 'on/off' : ")
                admin.loan_system(status,bank)

            elif ch == 7:
                break
            else:
               print('Invalid input')

    elif ch == 3:
       break
    else:
       print('Invalid input')
       