ACCOUNT_NUMBER=int(input("Enter your account number:"))
HOLDER_NAME=input("Enter your name:")
IFSC_CODE=input("Enter your IFSC code:")

def bank_account():
    print("---------Welcome----------")
    card=input("Please insert your card")

def choose_options():
    choose_option=int(input("1 DEPOSIT\n2 CASH WITHDRAW\n3 CHECK BALANCE\n4 CHANGE PIN  "   ))
    print("Choose your option")

def deposit_amounts():
    
    if choose_option==1:
        deposit_amount=int(input("Enter the amount you want to deposit:"))
        print("your amount",deposit_amount, "has been deposited sucessfully")
def cash_withdraw():
    if choose_option==2:
        withdraw_option=int(input("1 SAVING \n2 current"))
def check_balance():
    if choose_option==3:
        print("BALANCE AMOUNT:",Balance)
        return choose_option
def change_pin():
    if choose_option==4:
        old_pin=int(input("Enter your current pin:"))
        new_pin=int(input("Enter your new pin:"))
        print("your pin has been changed")
        return choose_option
    
        
    else:
        return card
    user_input=int(input("Enter the amount:"))
    if _input>deposit_amount:
        print("your available account balance is",deposit_amount)
        print("please re_try again")
        return choose_option
    pin_info=input("\nEnter 4-digit account pin:")
    if len(pin_info)==4:
        print("wait a moment")
    else:
        print("Please enter valid pin")
        return choose_option
    reciept_option=input("Do you want reciept:")
    if reciept_option=="yes":
        print("yes")
    else:
        return user_input
    balance=deposit_amount-user_input
    print("ACCOUNT NUMBER :",ACCOUNT_NUMBER)
    print("HOLDER NAME:",HOLDER_NAME)
    print("BALANCE:",balance)
bank_account()
choose_options()
deposit_amount()
cash_withdraw()
check_balance()
change_pin()