from read import *
from write import *
from datetime import datetime

def header():
    """Course Work : Fundametals of Computing"""
    print(header.__doc__)
    print("\n")
    print("\t \t \t \t \t \tWelcome to  Event Rental Shop")
    print("\t \t \t \t \t \t   Kathmandu, Nepal")
    print("\t \t \t \t \t \t Contact No: 1234567890")
    print("\n")
    print("#### Choose a option your option you want to continue ####")
    print("Enter 1: Rent. ")
    print("Enter 2: Return. ")
    print("Enter 3: Exit.")
    print("\n")

def user():
    _name = input("Enter your name: ")
    _phone = None
    
    while True:
        try:
            _phone = input("Enter your phone number: ")
            if not _phone.isdigit() or len(_phone) != 10:
                raise ValueError("Give a Valid 10-digit Phone Number")
            else:
                break  
        except ValueError as e:
            print(e)

    return _name, _phone


def item_id():
    while True:
        try:
            valid_id = int(input("Enter the id of the item you want to rent: "))
            return valid_id
        except ValueError:
            print("Invalid input. Please enter a valid integer ID.")

def item_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity you want to rent: "))
            return quantity
        except ValueError:
            print("Invalid input. Please enter a valid integer quantity.")

def num_days():
    while True:
        try:
            days = int(input("Enter the number of days you want to rent: "))
            if days <= 5:
                return days
            else:
                print("You can only rent items for 5 days or less. Please enter a valid number of days.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    

def continue_renting():
    while True:
        ask = input("Do you want to borrow any more items? If yes, press 'Y', or press Enter: ").upper()
        if ask == 'Y' or not ask:
            return ask
        else:
            print("Invalid input. Please enter 'Y' or press Enter to continue.")

def rents():
    myDictionary = create_dictionary()
    _name, _phone = user()
    
    print("\n")

    items_array = []

    rent_more = True

    while rent_more:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("S.N. \t\tItem Name     \t\t\t\t\tBrand Name        \t\t       Price\t      \t\t\t      Quantity")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")

        item_display()

        valid_id = item_id()
        while valid_id < 0 or valid_id > len(myDictionary):
            print("Enter a correct or valid id")
            valid_id = item_id()
        
        quantity = item_quantity()
        total_quantity = int(myDictionary[valid_id][3])
        while quantity <= 0 or quantity > total_quantity:
            print("The quantity you are looking for is not available at the moment.\n")
            quantity = item_quantity()
        
        

        item_name = myDictionary[valid_id][0]
        item_price = myDictionary[valid_id][2]
        selected_item_price = myDictionary[valid_id][2].replace("$", "")
        total_bill = int(selected_item_price) * quantity

        items_array.append(
             [item_name, quantity, item_price, total_bill]
        )

        updated_quantity = int(total_quantity) - int(quantity)
        myDictionary[valid_id][3] = str(updated_quantity)
        update_item_quantity(myDictionary)

        ask = continue_renting()
        if ask != "Y":
            days = num_days()
            rent_more = False

    today_date_and_time = datetime.now()
    rented_date = today_date_and_time.strftime("%Y-%m-%d")
     
    
    print("\n")
    print("\t \t \t \t \t \tWelcome to Global Events")
    print("\t \t \t \t \t \t  Tahachal, Kathmandu")
    print("\t \t \t \t \t \t Contact No: 9801132963")
    print("---------------------------------------------------------------------------------------------------------------")
    print("Customer Details")
    print("---------------------------------------------------------------------------------------------------------------")
    print("Name of the customer:", str(_name).upper())
    print("Contact number:", str(_phone))
    print("Date and time of renting:", rented_date)
    print("Number of days item rented:", days, "#Items can be rented for 5 days only.")
    print("---------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t \t   Rented Items Details")
    print("---------------------------------------------------------------------------------------------------------------")

    print("Item Name \t\t\t\t\t        Quantity \t     Unit Price \t\tTotal")
    print("---------------------------------------------------------------------------------------------------------------")
    total = 0
    for i in items_array:
        print(i[0], "\t\t\t", i[1], "\t\t\t", str(i[2]),  "${}".format(i[3]))
        total += int(i[3])
    print("---------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t            Grand Total: ${}".format(total))
    print("---------------------------------------------------------------------------------------------------------------")
    print("\n")
    create_invoice(_name, _phone, rented_date, days, items_array, total)

def fine(days_of_return, _name , _phone): 
    base_fine = 0  
    if days_of_return > 5:
        additional_days = days_of_return - 5
        fine_per_5_days = 10  
        base_fine = additional_days // 5 * fine_per_5_days 
        total = amt_to_pay(_name, _phone) 
        fine_added_amt = total + base_fine
    return base_fine, fine_added_amt


def update_list_txt(returned_items):
    myDictionary = create_dictionary()
    for item_data in returned_items:
        item_name = item_data[0]
        returned_quantity = int(item_data[1])
        
        for item_id, item_info in myDictionary.items():
            if item_info[0] == item_name:
                current_quantity = int(item_info[3])
                updated_quantity = current_quantity + returned_quantity
                item_info[3] = str(updated_quantity)
                break
    update_item_quantity(myDictionary)

def returns():
    _name, _phone = user()
    display_invoice(_name, _phone)
    days_of_return = int(input("Enter the number of return days."))
    base_fine, fine_added_amt= fine(days_of_return, _name , _phone)
    amt_to_pay(_name, _phone)
    returned_items = rented_item_list(_name, _phone)
    update_list_txt(returned_items)
    update_invoice(_name, _phone, base_fine, fine_added_amt)
    update_invoce_txt(_name, _phone, returned_items)
    display_invoice(_name, _phone)

def exit():
    while True:
        response = input("Do you want to exit the program? (Yes/No): ").strip().lower()
        if response == 'yes' or response == 'y':
            print("Thank you for using our system.")
            return True
        elif response == 'no' or response == 'n':
            return False
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")