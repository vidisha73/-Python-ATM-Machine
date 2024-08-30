class AtmMachine:
    password = 1234
    balance = 0

    @staticmethod
    def check_balance():
        print(f"Balance: {AtmMachine.balance}")

    @staticmethod
    def deposit(amt):
        AtmMachine.balance += amt
        print("Amount deposited successfully\n")

    @staticmethod
    def withdraw(amt):
        if AtmMachine.balance < amt:
            print("Balance insufficient")
        else:
            AtmMachine.balance -= amt
            print("Amount withdrawn successfully\n")

def main():
   
        print("Please insert your ATM card!!")

        pin = int(input("\nPlease enter your pin: "))

        attempt = 3
        while pin != AtmMachine.password and attempt > 0:
            attempt -= 1
            print("\nWrong password entered!")
            if attempt > 0:
                print(f"You have remaining {attempt} try!")
                print("Please try again")
            else:
                print("\nAccess denied")
                print("No attempts left")
                print("Please try after some time\n")
            pin = int(input())
            
        if pin == AtmMachine.password:
            print("Password entered correctly")
            c = 'y'
            while c == 'y':
                print("1: Check Balance")
                print("2: Withdraw amount")
                print("3: Deposit Amount")
                print("4: Exit\n")

                ch = int(input("Please enter your choice: "))

                if ch == 1:
                    AtmMachine.check_balance()
                elif ch == 2:
                    amt = int(input("Please enter amount to be withdrawn: "))
                    AtmMachine.withdraw(amt)
                    AtmMachine.check_balance()
                elif ch == 3:
                    amount = int(input("Please enter amount to be deposited: "))
                    AtmMachine.deposit(amount)
                    AtmMachine.check_balance()
                elif ch == 4:
                    sys.exit(0)
                else:
                    print("Wrong choice entered\n")

                c = input("\nDo you wish to continue(y/n)? ").lower()

   
if __name__ == "__main__":
    main()
