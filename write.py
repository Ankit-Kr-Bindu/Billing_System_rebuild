from read import *

def update_item_quantity(updated_dictionary):
    with open("item.txt", "w") as file:
        for values in updated_dictionary.values():
            file.write(str(values[0]) + "," + str(values[1]) + ","+ str(values[2]) + ","+ str(values[3]) + "," )
            file.write("\n")

def create_invoice(_name, _phone, rented_date, days, items_array, total):
    with open(f"{_name}_{_phone}.txt", 'w') as file:
        file.write("\n")
        file.write(f"\t\t\t\t\t\t\t  Welcome to Event Equipment Rental Shop\n")
        file.write(f"\t\t\t\t\t\t\t             Kathmandu, Nepal\n")
        file.write("\n")
        file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t             Customer Details\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write(f"Name of the customer: {_name.upper()}\n")
        file.write(f"Contact number: {_phone}\n")
        file.write(f"Date and time of renting: {rented_date}\n")
        file.write(f"Date and time of renting: {days}\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t             Items Details\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

        file.write("Item Name \t\t\t\t\t     Quantity \t\t             Unit Price \t\t\t\t               Amount\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for i in items_array:
            file.write(f"{i[0]}\t\t\t{i[1]}\t\t\t\t{i[2]}\t\t\t\t${i[3]}\n")


        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t          Total Amount: ${}\n".format(total))
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\n")
    return _name, _phone, days, rented_date, total

#return

def update_invoice(_name, _phone, base_fine, fine_added_amt):
    with open(f"{_name}_{_phone}.txt", 'a') as file:
            file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Fine Amount: ${}\n".format(base_fine))
            file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Grand Total: ${}\n".format(fine_added_amt))
            file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

def update_invoce_txt(_name, _phone, returned_items):
    file_name = f"{_name}_{_phone}_returned.txt"
    
    with open(file_name, 'w') as file:
        file.write("\n")
        file.write(f"\t\t\t\t\t\t\t  Returned Item Details\n")
        file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t             Customer Details\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write(f"Name of the customer: {_name.upper()}\n")
        file.write(f"Contact number: {_phone}\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t             Returned Items\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

        file.write("Item Name \t\t\t\t\t     Quantity\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for item_name, item_quantity in returned_items:
            file.write(f"{item_name}\t\t\t{item_quantity}\n")

    print("Returned items written to file:", file_name)
    return file_name  