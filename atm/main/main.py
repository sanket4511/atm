# step 1:
account = {"pin": 1234, "balance": 5000, "txns": []}

print("Welcome to ATM")

# PIN validation
tries = 0
while tries < 3:
    pin = int(input("Enter PIN: "))
    if pin == account["pin"]:
        print("Login successful\n")
        break
    else:
        print("Incorrect PIN\n")
        tries += 1

if tries == 3:
    print("Card Blocked!!")
    exit()

while True:
    print("""
    1. Check Balance
    2. Withdraw
    3. Deposit
    4. Change PIN
    5. Mini Statement
    6. Exit
    """)

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", account["balance"])

    elif choice == 2:
        amt = int(input("Withdraw amount: "))
        if amt <= account["balance"]:
            account["balance"] -= amt
            account["txns"].append(f"Withdraw: -{amt}")
            print("Collect cash.")
        else:
            print("Insufficient balance")
    elif choice == 3:
        amt = int(input("Deposit amount: "))
        if amt > 0:
            account["balance"] += amt
            account["txns"].append(f"Deposit: +{amt}")
            print("Cash Deposited")
        else:
            print("invalid amount")
    elif choice == 4:
        old_pin = int(input("Enter an  old PIN:"))
        if old_pin == account["pin"]:
            new_pin = int(input("Enter an new PIN: "))
            account["pin"] = new_pin
            print("PIN Chnage succesfully")
        else:
            print("INcorrect Pin")
    elif choice == 5:
        break

