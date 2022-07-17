from Car import car
import csv 
import os

class car_dl:
    """The data layer for the aapplication. The update_car method uses
       a string kms_reading parameter, not an int one."""
    cars_list = []
    
    @staticmethod
    def add_car_into_list(car):
        car_dl.cars_list.append(car)
        
    @staticmethod
    def get_car(license_plate):
        for store_car in car_dl.cars_list:
            if store_car.license_plate == license_plate:
                return store_car
        
        return None
        
    @staticmethod
    def update_car(license_plate,kms_reading):
        for store_car in car_dl.cars_list:
            if store_car.license_plate == license_plate:
                store_car.kms_reading = int(kms_reading)
                
    @staticmethod
    def delete_car(license_plate):
          for store_car in car_dl.cars_list:
            if store_car.license_plate == license_plate:
                car_dl.cars_list.remove(store_car)
                
    @staticmethod
    def read_car():
        path = "car_data.txt"
        if os.path.exists(path):
            with open(path) as file_variable:
                read_lines = file_variable.read().split("\n")
                
                for line in read_lines:
                    split = line.split(",")
                    if(len(split) != 1):
                        license_plate , chassis_no , engine_no , kms_reading = split[0],split[1],split[2],split[3]
                        kms_reading = int(kms_reading)
                        read_car = car(license_plate,chassis_no,engine_no,kms_reading)
                        car_dl.cars_list.append(read_car)
    
    @staticmethod
    def write_car():
        path = "car_data.txt"
        with open(path , "w") as fobj:
            for store_car in car_dl.cars_list:
                fobj.write(store_car.license_plate+","+store_car.chassis_no+","+store_car.engine_no+","+str(store_car.kms_reading)+"\n")
                