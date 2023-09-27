#write in read.py file

def create_dictionary():
    
    myDictionary = {}
    with open("item.txt", "r") as file:
        item_id = 1
   
        for line in file:
            line = line.replace("\n", "")
            myDictionary[item_id] = line.split(",")
            item_id = item_id + 1

        return myDictionary
    
def item_display():
    with open("item.txt", "r") as file:
        i = 1 
        for line in file:
            print(i, "\t\t"+ line.replace(",","\t\t"))
            i = i+1

def display_invoice(_name, _phone):
    file_name = f"{_name}_{_phone}.txt"
    try:
        with open(file_name, "r") as file:
            invoice_details = file.readlines()
            
        for line in invoice_details:
            print(line.rstrip("\n"))
    except FileNotFoundError:
        print("No such invoice found.")

def amt_to_pay(_name, _phone):
    file_name = f"{_name}_{_phone}.txt"
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if "Total Amount: $" in line:
                    total = float(line.split("$")[1])
                    return total
        
    except FileNotFoundError:
        print("No existing bill found for the user.") 

def rented_item_list(_name, _phone):
    file_name = f"{_name}_{_phone}.txt"
    returned_items = []
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            found_items_section = False
            for line in lines:
                if "Items Details" in line:
                    found_items_section = True
                elif found_items_section and not line.strip():
                    break  
                elif found_items_section:
                    item_data = line.strip().split('\t\t\t')
                    if len(item_data) >= 4 and item_data[1]:  
                        item_name = item_data[0]
                        item_quantity = item_data[1].strip()
                        returned_items.append((item_name, item_quantity))
    except FileNotFoundError:
        print("No existing bill found for the user.")
    return returned_items