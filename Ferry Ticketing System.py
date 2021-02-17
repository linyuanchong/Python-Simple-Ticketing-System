#main menu
def main_menu():
    print("FERRY TICKETING SYSTEM OF COMPANY LALALA")
    print("P - to Purchase Ticket")
    print("V - to View Seating Arrangement")
    print("Q - to Quit the system")
    user_choice1 = str(input("Go to: ")) #user to select next step

    if user_choice1 == "P" or user_choice1 == "p":
        time_and_place_and_class()
    #havent done for seat arrangement!!!!
    elif user_choice1 == "V" or user_choice1 == "v":
        seats_arg()
    elif user_choice1 == "Q" or user_choice1 == "q":
        quit()
    else:
        print("Please insert a valid input!")
        print("\n")
        main_menu()



#Submenu
#user to choose time & destination
def time_and_place_and_class():
    print("Please Select a Departure")
    print(" Penang to Langwaki - 1 \n Langkawi to Penang - 2")
    user_choice3 = input("Enter The Place You Wish To Depart From: ")
    print("Please Select a Trip Time")
    print(" 10:00am - 1 \n 11:00am - 2 \n 12:00pm - 3 \n 1:00pm - 4 \n 2:00pm - 5 \n 3:00pm - 6 \n 4:00pm - 7 \n 5:00pm - 8")
    user_choice4 = input("Enter The Time You Wish To Depart: ")  

    print("FERRY TICKETING SYSTEM OF COMPANY LALALA")
    print("PURCHASING MODULE")
    print("B - to Purchase Ticket for Business Class")
    print("E - to Purchase Ticket for Economy Class")
    print("M - to Return to Main Menu")
    user_choice2 = str(input("Go to -")) #user to select next step
#penang to langkawi business class
    if user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "1" and user_choice4 == "1":
        seat_assigned_B("ferry001a.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "1" and user_choice4 == "2":
        seat_assigned_B("ferry002a.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "1" and user_choice4 == "3":
        seat_assigned_B("ferry003a.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "1" and user_choice4 == "4":
        seat_assigned_B("ferry004a.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "1" and user_choice4 == "5":
        seat_assigned_B("ferry005b.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "1" and user_choice4 == "6":
        seat_assigned_B("ferry006b.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "1" and user_choice4 == "7":
        seat_assigned_B("ferry007b.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "1" and user_choice4 == "8":
        seat_assigned_B("ferry008b.txt")
#langkawi to penang business class
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "2" and user_choice4 == "1":
        seat_assigned_B("ferry005a.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "2" and user_choice4 == "2":
        seat_assigned_B("ferry006a.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "2" and user_choice4 == "3":
        seat_assigned_B("ferry007a.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "2" and user_choice4 == "4":
        seat_assigned_B("ferry008a.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "2" and user_choice4 == "5":
        seat_assigned_B("ferry001b.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "2" and user_choice4 == "6":
        seat_assigned_B("ferry002b.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "2" and user_choice4 == "7":
        seat_assigned_B("ferry003b.txt")
    elif user_choice2 == "B" or user_choice2 == "b" and user_choice3 == "2" and user_choice4 == "8":
        seat_assigned_B("ferry004b.txt")
#penang to langkawi economy class
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "1" and user_choice4 == "1":
        seat_assigned_E("ferry001a.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "1" and user_choice4 == "2":
        seat_assigned_E("ferry002a.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "1" and user_choice4 == "3":
        seat_assigned_E("ferry003a.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "1" and user_choice4 == "4":
        seat_assigned_E("ferry004a.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "1" and user_choice4 == "5":
        seat_assigned_E("ferry005b.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "1" and user_choice4 == "6":
        seat_assigned_E("ferry006b.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "1" and user_choice4 == "7":
        seat_assigned_E("ferry007b.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "1" and user_choice4 == "8":
        seat_assigned_E("ferry008b.txt")
#langkawi to penang economy class
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "2" and user_choice4 == "1":
        seat_assigned_E("ferry005a.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "2" and user_choice4 == "2":
        seat_assigned_E("ferry006a.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "2" and user_choice4 == "3":
        seat_assigned_E("ferry007a.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "2" and user_choice4 == "4":
        seat_assigned_E("ferry008a.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "2" and user_choice4 == "5":
        seat_assigned_E("ferry001b.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "2" and user_choice4 == "6":
        seat_assigned_E("ferry002b.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "2" and user_choice4 == "7":
        seat_assigned_E("ferry003b.txt")
    elif user_choice2 == "E" or user_choice2 == "e" and user_choice3 == "2" and user_choice4 == "8":
        seat_assigned_E("ferry004b.txt")
    

#assign seat after user made their choice
def seat_assigned_B(file_name):
    myfile = open(file_name, 'r')
    data = myfile.readlines()
    count = 1
    i = 6 
    while i == 6:
        if data[i] == "A *    0   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat AI assigned")
            del data[i]
            data.insert(6, "A *    1   *   0   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "A *    1   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat AII assigned")
            del data[i]
            data.insert(6, "A *    1   *   1   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "A *    1   *   1   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat AIII assigned")
            del data[i]
            data.insert(6, "A *    1   *   1   *   1   *   0   *   0    *\n")
            break
        
        elif data[i] == "A *    1   *   1   *   1   *   0   *   0    *\n":
            print("seats available")
            print("Seat AIV assigned")
            del data[i]
            data.insert(6, "A *    1   *   1   *   1   *   1   *   0    *\n")
            break
        
        elif data[i] == "A *    1   *   1   *   1   *   1   *   0    *\n":
            print("seats available")
            print("Seat AV assigned")
            del data[i]
            data.insert(6, "A *    1   *   1   *   1   *   1   *   1    *\n")
            break
        
        count = count + 1
        if count == 2:
            break

    while count == 2:
        i = 7
        if data[i] == "B *    0   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat BI assigned")
            del data[i]
            data.insert(7, "B *    1   *   0   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "B *    1   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat BII assigned")
            del data[i]
            data.insert(7, "B *    1   *   1   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "B *    1   *   1   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat BIII assigned")
            del data[i]
            data.insert(7, "B *    1   *   1   *   1   *   0   *   0    *\n")
            break
        
        elif data[i] == "B *    1   *   1   *   1   *   0   *   0    *\n":
            print("seats available")
            print("Seat BIV assigned")
            del data[i]
            data.insert(7, "B *    1   *   1   *   1   *   1   *   0    *\n")
            break
        
        elif data[i] == "B *    1   *   1   *   1   *   1   *   0    *\n":
            print("seats available")
            print("Seat BV assigned")
            del data[i]
            data.insert(7, "B *    1   *   1   *   1   *   1   *   1    *\n")
            break

        elif data[i] == "B *    1   *   1   *   1   *   1   *   1    *\n":
            print("All seats are full, would you like to consider switching to Economy Class?")
            user_switch=input("Y-Yes \nN-No \nPlease select:  ")
            if user_switch=="Y" or user_switch=="y":
                seat_assigned_E(file_name)
            elif user_switch=="N" or user_switch=="n":
                print("Well, thank you for using Company LALALA, we hope we can serve you better in the future :)")
                main_menu()
            break
        
        count = count + 1
        if count == 3:
            break
        
    myfile = open(file_name,"w+")
    for i in range(20):
        myfile.write(data[i])
    myfile.close()

def seat_assigned_E(file_name):
    myfile = open(file_name, 'r')
    data = myfile.readlines()
    count = 1
    i = 11 
    while i == 11:
        if data[i] == "C *    0   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat CI assigned")
            del data[i]
            data.insert(11, "C *    1   *   0   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "C *    1   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat CII assigned")
            del data[i]
            data.insert(11, "C *    1   *   1   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "C *    1   *   1   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat CIII assigned")
            del data[i]
            data.insert(11, "C *    1   *   1   *   1   *   0   *   0    *\n")
            break
        
        elif data[i] == "C *    1   *   1   *   1   *   0   *   0    *\n":
            print("seats available")
            print("Seat CIV assigned")
            del data[i]
            data.insert(11, "C *    1   *   1   *   1   *   1   *   0    *\n")
            break
        
        elif data[i] == "C *    1   *   1   *   1   *   1   *   0    *\n":
            print("seats available")
            print("Seat CV assigned")
            del data[i]
            data.insert(11, "C *    1   *   1   *   1   *   1   *   1    *\n")
            break
        
        count = count + 1
        if count == 2:
            break

    while count == 2:
        i = 12
        if data[i] == "D *    0   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat DI assigned")
            del data[i]
            data.insert(12, "D *    1   *   0   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "D *    1   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat DII assigned")
            del data[i]
            data.insert(12, "D *    1   *   1   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "D *    1   *   1   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat DIII assigned")
            del data[i]
            data.insert(12, "D *    1   *   1   *   1   *   0   *   0    *\n")
            break
        
        elif data[i] == "D *    1   *   1   *   1   *   0   *   0    *\n":
            print("seats available")
            print("Seat DIV assigned")
            del data[i]
            data.insert(12, "D *    1   *   1   *   1   *   1   *   0    *\n")
            break
        
        elif data[i] == "D *    1   *   1   *   1   *   1   *   0    *\n":
            print("seats available")
            print("Seat DV assigned")
            del data[i]
            data.insert(12, "D *    1   *   1   *   1   *   1   *   1    *\n")
            break
        count = count + 1
        if count == 3:
            break
    while count == 3:
        i = 13
        if data[i] == "E *    0   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat EI assigned")
            del data[i]
            data.insert(13, "E *    1   *   0   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "E *    1   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat EII assigned")
            del data[i]
            data.insert(13, "E *    1   *   1   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "E *    1   *   1   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat EIII assigned")
            del data[i]
            data.insert(13, "E *    1   *   1   *   1   *   0   *   0    *\n")
            break
        
        elif data[i] == "E *    1   *   1   *   1   *   0   *   0    *\n":
            print("seats available")
            print("Seat EIV assigned")
            del data[i]
            data.insert(13, "E *    1   *   1   *   1   *   1   *   0    *\n")
            break
        
        elif data[i] == "E *    1   *   1   *   1   *   1   *   0    *\n":
            print("seats available")
            print("Seat EV assigned")
            del data[i]
            data.insert(13, "E *    1   *   1   *   1   *   1   *   1    *\n")
            break
        count = count + 1
        if count == 4:
            break

    while count == 4:
        i = 14
        if data[i] == "F *    0   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat FI assigned")
            del data[i]
            data.insert(14, "F *    1   *   0   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "F *    1   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat FII assigned")
            del data[i]
            data.insert(14, "F *    1   *   1   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "F *    1   *   1   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat FIII assigned")
            del data[i]
            data.insert(14, "F *    1   *   1   *   1   *   0   *   0    *\n")
            break
        
        elif data[i] == "F *    1   *   1   *   1   *   0   *   0    *\n":
            print("seats available")
            print("Seat FIV assigned")
            del data[i]
            data.insert(14, "F *    1   *   1   *   1   *   1   *   0    *\n")
            break
        
        elif data[i] == "F *    1   *   1   *   1   *   1   *   0    *\n":
            print("seats available")
            print("Seat FV assigned")
            del data[i]
            data.insert(14, "F *    1   *   1   *   1   *   1   *   1    *\n")
            break
        count = count + 1
        if count == 5:
            break
        
    while count == 5:
        i = 15
        if data[i] == "G *    0   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat GI assigned")
            del data[i]
            data.insert(15, "G *    1   *   0   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "G *    1   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat GII assigned")
            del data[i]
            data.insert(15, "G *    1   *   1   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "G *    1   *   1   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat GIII assigned")
            del data[i]
            data.insert(15, "G *    1   *   1   *   1   *   0   *   0    *\n")
            break
        
        elif data[i] == "G *    1   *   1   *   1   *   0   *   0    *\n":
            print("seats available")
            print("Seat GIV assigned")
            del data[i]
            data.insert(15, "G *    1   *   1   *   1   *   1   *   0    *\n")
            break
        
        elif data[i] == "G *    1   *   1   *   1   *   1   *   0    *\n":
            print("seats available")
            print("Seat GV assigned")
            del data[i]
            data.insert(15, "G *    1   *   1   *   1   *   1   *   1    *\n")
            break
        count = count + 1
        if count == 6:
            break
        
    while count == 6:
        i = 16
        if data[i] == "H *    0   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat HI assigned")
            del data[i]
            data.insert(16, "H *    1   *   0   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "H *    1   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat HII assigned")
            del data[i]
            data.insert(16, "H *    1   *   1   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "H *    1   *   1   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat HIII assigned")
            del data[i]
            data.insert(16, "H *    1   *   1   *   1   *   0   *   0    *\n")
            break
        
        elif data[i] == "H *    1   *   1   *   1   *   0   *   0    *\n":
            print("seats available")
            print("Seat HIV assigned")
            del data[i]
            data.insert(16, "H *    1   *   1   *   1   *   1   *   0    *\n")
            break
        
        elif data[i] == "H *    1   *   1   *   1   *   1   *   0    *\n":
            print("seats available")
            print("Seat HV assigned")
            del data[i]
            data.insert(16, "H *    1   *   1   *   1   *   1   *   1    *\n")
            break
        count = count + 1
        if count == 7:
            break
        
    while count == 7:
        i = 17
        if data[i] == "J *    0   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat JI assigned")
            del data[i]
            data.insert(17, "J *    1   *   0   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "J *    1   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat JII assigned")
            del data[i]
            data.insert(17, "J *    1   *   1   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "J *    1   *   1   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat JIII assigned")
            del data[i]
            data.insert(17, "J *    1   *   1   *   1   *   0   *   0    *\n")
            break
        
        elif data[i] == "J *    1   *   1   *   1   *   0   *   0    *\n":
            print("seats available")
            print("Seat JIV assigned")
            del data[i]
            data.insert(17, "J *    1   *   1   *   1   *   1   *   0    *\n")
            break
        
        elif data[i] == "J *    1   *   1   *   1   *   1   *   0    *\n":
            print("seats available")
            print("Seat JV assigned")
            del data[i]
            data.insert(17, "J *    1   *   1   *   1   *   1   *   1    *\n")
            break
        count = count + 1
        if count == 8:
            break
    while count == 8:
        i = 18
        if data[i] == "K *    0   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat KI assigned")
            del data[i]
            data.insert(18, "K *    1   *   0   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "K *    1   *   0   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat KII assigned")
            del data[i]
            data.insert(18, "K *    1   *   1   *   0   *   0   *   0    *\n")
            break
        
        elif data[i] == "K *    1   *   1   *   0   *   0   *   0    *\n":
            print("seats available")
            print("Seat KIII assigned")
            del data[i]
            data.insert(18, "K *    1   *   1   *   1   *   0   *   0    *\n")
            break
        
        elif data[i] == "K *    1   *   1   *   1   *   0   *   0    *\n":
            print("seats available")
            print("Seat KIV assigned")
            del data[i]
            data.insert(18, "K *    1   *   1   *   1   *   1   *   0    *\n")
            break
        
        elif data[i] == "K *    1   *   1   *   1   *   1   *   0    *\n":
            print("seats available")
            print("Seat KV assigned")
            del data[i]
            data.insert(18, "K *    1   *   1   *   1   *   1   *   1    *\n")
            break

        elif data[i] == "K *    1   *   1   *   1   *   1   *   1    *\n":
            print("All seats are full, would you like to consider switching to the another ferry?")
            user_switch=input("Y-Yes \nN-No \nPlease select:  ")
            if user_switch=="Y" or user_switch=="y":
                time_and_place_and_class
            elif user_switch=="N" or user_switch=="n":
                print("Well, thank you for using Company LALALA, we hope we can serve you better in the future :)")
                main_menu()
            break
        
        count = count + 1
        if count == 9:
            break

    myfile = open(file_name,"w+")
    for i in range(20):
        myfile.write(data[i])
    myfile.close()













#boarding ticket (name, seat number, business/eonomy, date & time, source & destination
#of the trip & ferry ID

main_menu()




