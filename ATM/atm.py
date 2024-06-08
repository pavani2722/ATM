from cardHolder import cardHolder
    
def print_menu():
    ### print options to the user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("How much $$ would you like to deposit: " )) 
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you for your $$. Your new balance is: ",str(cardHolder.get_balance()))
    except:
        print("Invalid input")
def withdraw(cardHolder):
    try:
        withdraw = float(input("How much $$ would you like to withdraw: "))
        ## check if user has enough money
        if (cardHolder.get_balance() < withdraw):
            print("Insufficient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)    
            print("You 're good to go! Thank You :)") 
    except:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("","","","","") 

    ### creat a repo of cardholder

    list_of_cardHolder =[]
    list_of_cardHolder.append(cardHolder("4589456726793418", 5678, "Abhi", "Gandipadala", 200.31))
    list_of_cardHolder.append(cardHolder("4589689342493357", 7837, "Pavani", "Adduri", 150.80))
    list_of_cardHolder.append(cardHolder("6732456726795468", 3418, "John", "griffer", 120.31))
    list_of_cardHolder.append(cardHolder("6489456726793534", 9849, "Dawn", "Smith", 200.31))

    ###Prompt user for debit card number
    debitcardNum = ""
    while True:
        try:
            debitcardNum = input("Please insert Your debit card: ")
            ### check aganist repo
            debitMatch = [holder for holder in list_of_cardHolder if holder.cardNum == debitcardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again. ")
        except:
            print("card number not recognized. Please try again. ")

##prompt for PIN
while True:
    try:
        userPin = int(input("Pleae enter your pin :").strip())
        if (current_user.get_pin() == userPin):
            break
        else:
            print("Invalid PIN.Please try again. ")   
    except:
        print("Invalid PIN.Please try again. ") 

#####Print options
print("Welcome ", current_user.get_firstname(), " :)") 
option = 0
while(True):
    print_menu()
    try:
        option = int(input()) 
    except:
        print("Invalid input . Please try again. ")    

    if(option == 1):
        deposit(current_user)
    elif(option == 2):
        withdraw(current_user)
    elif(option == 3):
        check_balance(current_user)
    elif(option == 4):
        break
    else:
        option = 0
print("Thank you. Have a nice day :)")




            



