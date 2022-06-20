print("Welcome to Phone directory!")
print("You have 0 contacts saved")

Contact = {}

while True:
    def details():
        num = int(input("Enter the number you want to save: "))
        firstname = str(input("Enter the First name: "))
        lastname = str(input("Enter the last name: "))
        Email = input("Enter the Email(if any): ")

        Contact[f"{firstname} {lastname}"] = {}

        if firstname == "" and lastname == "":
            print("Enter a name to save")
            while True:
                firstname = str(input(f"Enter the firstname: "))
                lastname = str(input("Enter the lastname: "))
                if firstname != "" and lastname != "":
                    Contact["FirstName"]  = firstname
                    Contact["LastName"] = lastname
                    break
        else:
            Contact[f"{firstname} {lastname}"]["Firstname"] = firstname
            Contact[f"{firstname} {lastname}"]["LastName"] = lastname
            Contact[f"{firstname} {lastname}"]["Phone"] = num
            if Email == "":
                pass
            else:
                Contact[f"{firstname} {lastname}"]["Email"] = Email
        
        print(Contact)
        print("Saved successfully")
    details()
    
    que = str(input("Do you want to edit more? (y/n): "))
    def run():
        if que == "y":
            Options = '''
            ====What following operations do you want to enter?====
                    1. Save a Contact again
                    2. Deleting a contact
                    3. Edit an existing contact
                    4. Watch Contact details
                    5. Total Contacts
            '''

            print(Options)
            n = int(input("Enter a choice: "))

            if n == 1:
                details()

            elif n ==2:
                def deleting_contact():
                    print(Contact)
                    dele = str(input("Enter the contact you want to delete: "))
                    
                    del Contact[f"{dele}"]
                    print("Contacts deleted successfully")
                    print(Contact)

                deleting_contact()
            
            elif n == 3:
                print("Which contact do you want to edit?")
                edit = str(input("Enter the contact name: "))
                print(Contact[f"{edit}"])

                firstname = str(input("Enter the firstname: "))
                lastname =  str(input("Enter the lastname: "))
                numb = input("Enter the number: ")
                if firstname == "" and lastname == "" and numb == "":
                    pass
                else:
                    Contact[f"{firstname} {lastname}"]  = Contact[f"{edit}"] 
                    del Contact[f"{edit}"]
                    Contact[f"{firstname} {lastname}"]["Firstname"] = firstname
                    Contact[f"{firstname} {lastname}"]["LastName"] = lastname
                    Contact[f"{firstname} {lastname}"]["Phone"] = numb
                
                print("Contact edited successfully!")
                print(Contact)

            elif n == 4:
                print("Which contact detail do you want?")
                inp = str(input("Enter the name of the contact: "))
                print(Contact[f"{inp}"])

            elif n == 5:
                print(Contact)
            
            while True:
                ques = str(input("Do you want to edit more? (y/n): "))
                if ques == "y":
                    run()
                else:
                    break
                break                    
        else: 
            print("Thank You!")

    run()

    with open("Contacts.txt", "a") as f:
        f.write(str(Contact))
        f.write("\n")

    break

dic = len(Contact)
print(f"You have {dic} contact(s) saved")
# Your contacts are saved in the "Contacts.txt" file.

