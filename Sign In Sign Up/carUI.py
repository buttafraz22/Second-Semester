from car_dl import car_dl
from Car import car

class car_UI:
    @staticmethod
    def menu():
        print("1.Add Car")
        print("2.Check car Exist")
        print("3.Update Car")
        print("4.Delete Car")
        print("5. Exit")
        x = input("Enter your choice")
        return x
    
    @staticmethod
    def add_car():
        license_plate = input("Enter license Plate ")
        chassis_no = input("Enter chassis no ")
        engine_no = input("Enter Engine no")
        kms_reading = int(input("Enter kms Reading"))
        added_car = car(license_plate,chassis_no,engine_no,kms_reading)
        return added_car
    
    @staticmethod
    def check_car():
        license_plate = input("Enter license plate of the car you want to see: ")
        car_retrieved = car_dl.get_car(license_plate)
        if car_retrieved != None:
            print(car_retrieved.license_plate + " Exists.")
    
    @staticmethod
    def update_car():
        license_plate = input("Enter license plate of the car you want to see: ")
        car_retrieved = car_dl.get_car(license_plate)
        if car_retrieved != None:
            kms_reading = input("Enter updated value of kms: ")
            car_dl.update_car(license_plate,kms_reading)
     
    @staticmethod
    def delete_car():       
        license_plate = input("Enter license plate ")
        car_dl.delete_car(license_plate)
        print("Car has been deleted successfully.")