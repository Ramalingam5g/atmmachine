import time
class banking:
    def __init__(self,balance):
        self.balance=balance

    def pin_info(self):
        print("----WELCOME----")
        time.sleep(2)
        print("Please insert your card")
        time.sleep(2)        
        pin=int(input("Enter Your pin:"))
        
    def insert_card(self): 
        
       
        print(""".............PLEASE SELECT OPTION:............11
        1. DEPOSIT 
        2. CASH WITHDRAW 
        3. CHANGE PIN     
        4. BALANCE
        """)
        choose_option=int(input("Enter your option:"))
        if choose_option==1:
            self.deposit()
        if choose_option==2:
            self.withdraw()
        if choose_option==3:
            self.change_pin()
        if choose_option==4:
            self.Balance_Enquiry()
        
    
          
    def deposit(self):
        deposit=int(input("enter the amount you want be deposited:"))
        print("you amount",deposit,"has been deposited")
        current_balance=deposit + self.balance
        time.sleep(2)
        print("your current balance is:",current_balance)
        return self.insert_card()

    def withdraw(self):
        withdraw_option=int(input("1 SAVING \n2 CURRENT"))
        user_amount=int(input("Enter the amount:"))
        if user_amount>self.balance:
            print("Current balance is less then your withdrawl")
        else: 
            self.balance=(self.balance-withdrawl_amount)

        time.sleep(2)
        print("Your transcation being proceed....")
        time.sleep(2)
        print("Please collect  your cash")
        current_balance2=self.balance-user_amount
        print("your current balance:",current_balance2)
        time.sleep(2)
        return self.insert_card()


        
    def change_pin(self):
        old_pin=int(input("Enter your current pin:"))
        new_pin=int(input("Enter your new pin:"))
        
        if old_pin==new_pin:
            print("invalid")
            return self.insert_card()
        else:
            print("your pin has been changed")
            return self.insert_card()

    def Balance_Enquiry(self):
        
        print("Your balance amount:",self.balance)
        return self.insert_card()



obj=banking(10000)
obj.pin_info()
obj.insert_card()
obj.withdraw()
obj.change_pin()
obj.Balance_Enquiry()
