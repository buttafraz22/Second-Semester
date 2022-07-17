class car:
   # license_plate = " "
   # chassis_no = " "
   # engine_no = " "
   # kms_reading = " "
    def __init__(self,license_plate,chassis_no,engine_no,kms_reading):
        self.license_plate = license_plate
        self.engine_no = engine_no
        self.chassis_no = chassis_no
        self.kms_reading = kms_reading
        self.is_booked = False 
    