import login

class Medicine:
    def __init__(self, med_id, med_name, gen_name, com_name, quantity, price):
        self.med_id = med_id
        self.med_name = med_name
        self.gen_name = gen_name
        self.com_name = com_name
        self.quantity = quantity
        self.price = price

    def edit_quantity(self, new_quantity):
        self.quantity = new_quantity

    def edit_price(self, new_price):
        self.price = new_price

    def display_details(self):
        print(f"Medicine ID: {self.med_id}")
        print(f"Medicine Name: {self.med_name}")
        print(f"Generic Name: {self.gen_name}")
        print(f"Company Name: {self.com_name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")
        print('__________________________')

class Project:
    def __init__(self):
        self.medicines = {}
        self.med_code = 1

    def add_element(self):
        try:
            med_name = input('Enter Medicine Name: ')
            if med_name in self.medicines:
                print('Medicine Already Exists')
                return
            gen_name = input('Enter Generic Name: ')
            com_name = input('Enter Company Name: ')
            quantity = int(input('Enter Quantity: '))
            price = float(input('Enter Price: '))
            new_medicine = Medicine(self.med_code, med_name, gen_name, com_name, quantity, price)
            self.medicines[med_name] = new_medicine

            print('Successfully Added Medicine code : ', self.med_code)
            self.med_code += 1

        except (TypeError, ValueError):
            print("Invalid input. Please enter a valid value.")

    def list_display(self):
        for med_name, medicine in self.medicines.items():
            medicine.display_details()

    def search_by_code(self):
        try:
            code = int(input('Enter the Medicine code: '))
            for medicine in self.medicines.values():
                if medicine.med_id == code:
                    medicine.display_details()
                    self.edit_or_disable_medicine(medicine)
                    break
            else:
                print("Medicine not found with given code.")
        except (TypeError, ValueError):
            print("Invalid input. Please enter a valid value.")

    def search_by_name(self):
        try:
            med_name = input('Enter the Medicine name: ')
            if med_name in self.medicines:
                self.medicines[med_name].display_details()
                self.edit_or_disable_medicine(self.medicines[med_name])
            else:
                print("Medicine not found with given name.")
        except (TypeError, ValueError):
            print("Invalid input. Please enter a valid value.")

    def edit_or_disable_medicine(self, medicine):
        while True:
            print('''How would you like to proceed?
                1. Edit Medicine
                2. Disable Medicine
                3. Go back''')
            choice = int(input('Enter a Number: '))
            if choice == 1:
                print('''Which field do you want to edit?
                        1. Quantity
                        2. Price''')
                field_choice = int(input('Enter your choice: '))
                if field_choice == 1:
                    new_quantity = int(input("Enter new quantity: "))
                    medicine.edit_quantity(new_quantity)
                    print("Quantity updated successfully.")
                elif field_choice == 2:
                    new_price = float(input("Enter new price: "))
                    medicine.edit_price(new_price)
                    print("Price updated successfully.")
            elif choice == 2:
                disable_choice = input("Do you want to disable the Medicine? (y/n): ")
                if disable_choice.lower() == 'y':
                    del self.medicines[medicine.med_name]
                    print('Medicine Successfully Deleted')
                    break
                else:
                    print('No changes made.')
            elif choice == 3:
                return
            else:
                print("Invalid choice. Please choose a valid option.")

print('\t\t\t\t\t\t\t\t\t\t\t\t\tCLINICAL MANAGEMENT SYSTEM\n')
print('\t\t\t\t\t\t\t\t\t\t\t\t.......................................')
login.login()

username = 'BENISHA'
print('\t\t\t\t\t\t\t\t\t\t\t.......................................')
print(f'\t\t\t\t\t\t\t\t\t\t\t\t\t\tWELCOME {username}')
print('\t\t\t\t\t\t\t\t\t\t\t.......................................')

project = Project()
try:
    while True:
        print('''The Menu for You are:
            1. Add medicine
            2. See list of medicine
            3. Search and view medicine
            4. Go to main menu
            5. Exit
            ''')
        select = int(input('Enter your option: '))
        if select == 1:
            project.add_element()
        elif select == 2:
            print('The List Of Medicines Available Are:')
            project.list_display()
        elif select == 3:
            print('''How would You Like To Search For a Medicine?
                1. By Medicine Code
                2. By Medicine Name''')
            search_choice = int(input('Enter a Number: '))
            if search_choice == 1:
                project.search_by_code()
            elif search_choice == 2:
                project.search_by_name()
        elif select == 4:
            print('Going to Main Menu................')
        elif select == 5:
            break
        else:
            print("Invalid option. Please choose a valid number.")
except (TypeError, ValueError):
    print("Invalid input. Please enter a valid value.")
