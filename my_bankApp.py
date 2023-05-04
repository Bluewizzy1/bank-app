

class Bank:
    #   here, we initialize the attributes
    def __init__(self):
        self.client_details_list = []       #    an empty list that will store client details
        self.loggedin = False
        self.cash = 100
        self.TransferCash = False


    #   method is defined to create a new bank account for a client.
    def sign_up(self, name, ph, password):
        cash = self.cash
        conditions = True
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone Number! Please Enter 10 Digit Number")
            conditions = False

        # to check for the lenght of the password
        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5, and less than 18 characters")
            conditions = False

        if conditions == True:
            print("Account succesfully created")
            self.client_details_list = [name, ph, password]
            with open(f"{name}.txt", "w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")

    # to checks if the provided ph and password match any of the records
    def login(self, name, ph, password):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin = True

            if self.loggedin == True:
                print(f"{name} is logged in")
                self.cash = int(self.client_details_list[3])
                self.name = name
                self.ph = ph

            else:
                print("Wrong details")


    #    to update the cash balance of a client and record the deposit transaction in a text file.
    def deposit(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))

                self.update_history("deposit",amount,self.ph,self.ph,self.name,self.name)
                print("Amount deposited successfully")

        else:
            print("Enter correct value of amount")

    #    checks if the phone number given by the ph parameter matches the phone number of the client whose details were just read from the file.
    def transfer_cash(self, amount, name, ph):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")


        if str(ph) == self.client_details_list[1]:
            self.TransferCash = True

        if self.TransferCash == True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))

            with open(f"{self.name}.txt", "r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]), str(left_cash)))

            self.update_history("transfer",amount,ph,self.client_details_list[1],name,self.name)
            print("Amount Transfered Successfully to", name, "-", ph)
            print("Balance left =", left_cash)
        else:
            print("Oops!")

    #    this replaces the old password which is assumed to be the third element of client_details_list with the new password provided as a parameter to the method
    def password_change(self, password):
        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5, and less than 18 characters")
        else:
             with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

             with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(password)))
             print("New password set up successfully")

    #   this checks the loggedin if it is true, then grants user access to see consumated transaction.
    def history(self,ph):
        if self.loggedin == True:
            with open("transactions.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if str(ph) in line:
                        print(line.strip())
        else:
            print("Please log in first")    

    #   updates the transaction history file called "transactions.txt" with information about a new transaction
    def update_history(self,type,amount,ph,sender_ph,name,sender_name):
        with open("transactions.txt", "a") as f:
            f.write(f"{str(type).upper()} of {amount} to {ph}({name}) from {sender_ph}({sender_name}) \n")

#   check if code is being executed as the main program, then creates a new instance of Bank object
if __name__ == "__main__":
    Bank_object = Bank()
    print("Welcome to Blueworld Bank")
    print("1. Login")
    print("2. Create a new account")
    user = int(input("Make decision: "))
    print(user)
    # import pdb
    # pdb.set_trace()

    if user == 1:
        print("Logging in...")
        name = input("Enter name: ")
        ph = int(input("Enter phone number: "))
        password = input("Enter password: ")
        Bank_object.login(name, ph, password)
        while True:
            if Bank_object.loggedin:
                print("1. Make deposit")
                print("2. Balance check")
                print("3. Transfer")
                print("4. Edit profile")
                print("5. History")
                print("6. Logout")
                login_user = int(input())
                if login_user == 1:
                    print("Balance = $", Bank_object.cash)
                    amount = int(input("Enter amount:$ "))
                    Bank_object.deposit(amount)
                    print("\n1.back menu")
                    print("2. Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 2:
                    print("Balance = $", Bank_object.cash)
                    print("\n1.back menu")
                    print("2. Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 3:
                    print("Balance = $", Bank_object.cash)
                    amount = int(input("Enter amount: $"))
                    if amount > 0 and amount <= Bank_object.cash:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.transfer_cash(amount, name, ph)
                        print("\n1.back menu")
                        print("2. Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0 :
                        print("Enter please correct value of amount")

                    elif amount > Bank_object.cash:
                        print("Not enough balance")

                elif login_user == 4:
                    print("1. Password change")
                    print("2. Phone number change")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_password = input("Enter new password: ")
                        Bank_object.password_change(new_password)
                        print("\n1.back menu")
                        print("2. Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new phone number"))
                        Bank_object.ph_change(new_ph)
                        print("\n1.back menu")
                        print("2. Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                elif login_user == 5:
                    print("-----------ACCOUNT HISTORY-----------")
                    Bank_object.history(ph)
                    print("---------------------------------")
                    print("\n1.back menu")
                    print("2. Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        print("2. Thank you for banking with us")
                        break

                elif login_user == 6:
                    print("Logged out")
                    break
            else:
                print("Please login first")
    
    if user == 2:
        #   requesting input from a user to create a new bank account.
        print("Creating a new account")
        name = input("Enter name: ")
        ph = int(input("Enter phone number: ")) 
        password = input("Enter password: ")
        Bank_object.sign_up(name, ph, password)
