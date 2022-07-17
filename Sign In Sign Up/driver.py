from MUSerDL import MUserDL
from MUserUI import MUserUI
from carUI import car_UI
from car_dl import car_dl
import os
from time import sleep

def main(): #defining main function
    option = 0
    MUserDL.readFile()
    while True:
        option = MUserUI.menu()
        if(option == 3):
            break
        
        elif(option == 1):
            user = MUserUI.sign_in()
            check_user = MUserDL.SignIn(user)
            if(check_user.isAdmin):
                while True:
                    car_dl.read_car()
                    user_op = car_UI.menu()
                    
                    if user_op == "1":
                        add_car = car_UI.add_car()
                        car_dl.add_car_into_list(add_car)
                        car_dl.write_car()
                        
                    elif user_op == "2":
                        car_UI.check_car()
                        
                    elif user_op == "3":
                        car_UI.update_car()
                        car_dl.write_car()
                        
                    elif user_op == "4":
                        car_UI.delete_car()
                        car_dl.write_car()
                    
                    elif user_op == "5":
                        break
           
        
        elif(option == 2):
            user = MUserUI.sign_up()
            MUserDL.addUser(user)
            MUserDL.storeFile()    

main()