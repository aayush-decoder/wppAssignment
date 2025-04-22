
class Password_manager:
    pswList = []
    def __init__(self, password):
        self.password = password
        self.pswList.append(password)

    def set_new_psw(self, new_password):
        if new_password not in self.pswList:
            self.pswList.append(new_password)
        print("Your password has been updated!")

    def get_psw(self):
        return self.pswList[-1]
    
    def is_correct(self, givenPsw):
        return self.pswList[-1] == givenPsw
    

initial_psw = input("Enter initial password: ")
manager = Password_manager(initial_psw)

while True:
        print("""\nChoose an option:
            1. Set new password
            2. Check current password
            3. Get current password
            4. View password history
            5. Exit""")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            new_psw = input("Enter new password: ")
            manager.set_new_psw(new_psw)
        elif choice == "2":
            given = input("Enter psw to check: ")
            if manager.is_correct(given):
                print("Password is correct!")
            else:
                print("Passwird is incorrect!")
        elif choice == "3":
            print("Current password is: ", manager.get_psw())
        elif choice == "4":
            print("Password history: ", manager.pswList)
        elif choice == "5":
            print("Exited"); 
            break
        else:
            print("Invalid option, please try again.")



# rahul = Password_manager("abc")
# print(rahul.get_psw())
# rahul.set_new_psw('cook')
# rahul.set_new_psw('pizza')
# rahul.set_new_psw('cook')
# print(rahul.get_psw())
# print(rahul.pswList)