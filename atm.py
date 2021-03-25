ACCOUNT_NUMBER=int(input("Enter your account number:"))
HOLDER_NAME=input("Enter your name:")
IFSC_CODE=input("Enter your IFSC code:")
def bank_account():
    print("---------Welcome----------")
    card=input("Please insert your card")

def choose_options():
    print("Choose your option")
    choose_option=int(input("1 CASH WITHDRAW\n2 CHECK BALANCE\n3 CHANGE PIN\n4 DEPOSIT   "   ))

    print(choose_option)
    if choose_option==1:
        withdraw_option=int(input("1 SAVING \n2 current"))
    elif choose_option==2:
        print("BALANCE AMOUNT:",Balance)
        return choose_option
    elif choose_option==3:
        old_pin=int(input("Enter your current pin:"))
        new_pin=int(input("Enter your new pin:"))
        print("your pin has been changed")
        return choose_option
    elif choose_option==4:
        deposit_amount=int(input("Enter the amount you want to deposit:"))
        print("your amount",deposit_amount, "has been deposited sucessfully")
    else:
        return card
    user_input=int(input("Enter the amount:"))
    if _input>deposit_amount:
        print("your available account balance is",deposit_amount)
        print("please re_try again")
        return choose_option
    pin_info=int(input("\nEnter 4-digit account pin:"))
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
