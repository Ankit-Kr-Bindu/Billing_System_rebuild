from operations import *
from read import *
from write import *
from datetime import datetime



def main():
    
    loop = True
    while loop == True:
        header()   
        option = input("Choose the operation you want to continue: ")
        if option == '1':
            print("You are in now in Rent Interface.")
            rents()
            
            continue
        elif option == '2':
            print("You are in now in Return Interface.")
            returns()
            
        elif option == '3':
            if exit(): 
                break
            else:
                print("Continuing with the program...")           
main()