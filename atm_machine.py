print("-----Welcome to ATM-----")
accountInfo = {
    "Name": "Janhavi Patil",
    "Account_Number": 9098787676676,
    "Available_Balance": 20000,
    "PIN": 1234
}
pin = int(input("Enter your PIN...."))
if pin==accountInfo["PIN"]:
    print("Your pin is correct..")

    print("\n1.Check Balance...")
    print("2.Withdraw Amount ...")
    print("3.Deposit Amount...")
    print("4. Change PIN ...")
    print("5.Account Details ..")
    print("6. Exit ...")

    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Available Balance: ",accountInfo["Available_Balance"])
        case 2:
            w_amo=int(input("Enter withdraw amount: "))
            if w_amo>accountInfo["Available_Balance"]:
                print("Cannot withdraw not sufficient balance!!")
            else:
                print("withdraw successfully....")
        case 3:
            d_amo=int(input("Enter amount for deposit: "))
            n_amo=accountInfo["Available_Balance"]+d_amo
            print("Deposited successfully...")
            print("Updated Bank Balance:",n_amo)
        case 4:
            c_pin=int(input("Enter your new pin number: "))
            accountInfo["PIN"]==c_pin
            print("new pin is: ",c_pin)
        case 5:
            print("__Account Deatils__")
            print("Name:",accountInfo["Name"])
            print("Account Number:",accountInfo["Account_Number"])
            print("Available Balance:",accountInfo["Available_Balance"])
        case 6:
            print("EXIT......")
else:
    print("Invalid PIN entered!!!")

