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

def remove_existing(pb):
       query = str( input("Please Enetrthe name of the contact you wish to remove:"))
       temp = 0
       for i in range(len(pb)):
              if query == pb[i][0]:
                     temp += 1
                     print(pb.pop(i))
                     print("This query has now been removed")
                     return pb
        if temp == 0
                print("Sorry ,you have entered an invalid query. \nPlease recheck and try again later.")
                return pb 
def delete_all(pb):
       return pb.clear()
       
def search_existing(pb):
       choice = int(input("Enter search criteria\n\n\n 1. Name\n2. 2. Number\n3. 3. Email-Id\n4. DOB\n5. Category(Family/Friends/Work/Others)\ \nPlease enter:"))
       temp = []
       check = -1
       if choice == 1:
               query = str("Please enter the name of the contact you wish to search:))
               for i in range(len(pb)):
                      if query == pb[i][0]:
                             check = i
                             temp.append(pb[i])

       elif choice == 2:
              query = int(input("Please Enter the number of the con tact you wish to search"))
              for i in range(len(pb)):
                    if query ==pb[i][1]
                             check = i
                             temp.append(pb[i])

        elif choice == 3:
              query = str


        

        
        