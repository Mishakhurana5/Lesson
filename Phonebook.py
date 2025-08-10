import sys
def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")), 5
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter Contact %d details in the following order (ONLY):"  % (i+1))
        print("NOTE: * indicates mandatory fields")
print(".......................................................")
        temp = []
        for j in range(cols):
           if j == 0:
                   temp.append(str(input("Enter name*: ")))
                   if temp[j] == '' or temp[j] == ' ':
                           sys.exit("Name is a mandatory field. Process exiting due to blank field...")
            if j == 1:
                    temp.append(int(input("Enter number*: ")))
            if j == 2:
                    temp.append(str(input("Enter email address")))
                    if temp[j] == ' ' or temp[j] == ' ':
                           temp[j] = None
            if j == 3:
                    temp.append(str(input("Enter Date of birth(dd/mm/yy): ")))
                    if temp[j] == '' or temp[j] == ' ':
                           temp[j] = None
            if j == 4:
                    temp.append(str(input("Enter category (Family/Friend/Work/Others): ")))  
                    if temp[j] == "" or temp[j] == ' ':
                           temp[j] = None 
        phone_book.append(temp)
    print(phone_book)
    return phone_book


        
        