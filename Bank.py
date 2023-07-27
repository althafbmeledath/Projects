class Bank:
    
    def __init__(self):
        self.data={}
        self.money={}
        self.helper()
        self.number=None
        
    def helper(self):
        print("Press 1 to create new account")
        print("Press 2 to login")
        print("Press 3 to quit")
        
        choice=int(input("Enter your choice: "))
        if choice==1:
            self.create_new()
        elif choice==2:
            self.login()
            
        elif choice==3:
            return
        
    #function to create new account
    def create_new(self):
        number=input("Enter your number to create a new account: ")
        password1=input("Enter your password: ")
        password2=input("Renter your password to confirm: ")
        if password1==password2 and len(number)==10:
            self.data[number]=password2
            print("Account created successfully")
            self.money[number]=0
            return self.helper()
            
        else:
            print("Invalid mobile number or password")
            return self.helper()
        
    #function to login
    def login(self):
        number=input("Enter your number: ")
        password=input("Enter your password: ")
        #check if number and password is already saved or not
        if number in self.data.keys() and password in self.data.values():
            self.number=number
            
            print("Logged in successfully")
            return self.options()
        
        else:
            print("Invalid username or password")
            return self.helper()
        
    #options functions
    def options(self):
        print()
        print("Press 1 to deposit money")
        print("Press 2 to send money")
        print("Press 3 to withdraw your money")
        print("Press 4 to view balance")
        print("Press 5 to logout")
        choice=int(input("Enter your choice: "))
        if choice==1:
            return self.deposit()
        
        elif choice==2:
            return self.send()
        
        elif choice==3:
            return self.withdraw()
        
        elif choice==4:
            return self.v_balance()
        
        elif choice==5:
            return self.logout()
        
    #function to deposit money
    def deposit(self):
        money_d=int(input('Enter the amount in rs to deposit: '))
        self.money[self.number]=money_d
        print("Money deposited successfully")
        return self.options()
    
    #function to send money
    def send(self):
        n_number=input("Enter the number you want to send money to: ")
        if n_number in self.data.keys():
            s_money=int(input("Enter the amount of money you need to send: "))
            if s_money<(self.money[self.number]):
                self.money[n_number]+=s_money
                self.money[self.number]-=s_money
                print(f"Money send successfully , available balance is {self.money[self.number]}")
                return self.options()
            else:
                print("Insufficient Balance")
                return self.options()
        else:
            print('invalid number')
            return self.options()
        
    #function to withdraw money
    def withdraw(self):
        w_money=int(input("Enter the amout of money you need to withdraw: "))
        if w_money<self.money[self.number]:
            self.money[self.number]-=w_money
            print(f"Rs {w_money} withdrawn successfully and remaining balance is {self.money[self.number]}")
            return self.options()
        
    #function to view balance
    def v_balance(self):
        print(f"The balance is {self.money[self.number]}")
        return self.options()
    
    #function to logout
    def logout(self):
        return self.helper()
    
b=Bank()









