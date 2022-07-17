from MUser import MUser
import os.path

class MUserDL:
    usersList = []
    
    # creating static methods
    @staticmethod
    def addUser(user):
        MUserDL.usersList.append(user)
    
    @staticmethod
    def SignIn(user):
        for storedUser in MUserDL.usersList:
            if(storedUser.username == user.username and storedUser.password == user.password):
                return storedUser
        
        return None
    
    @staticmethod
    def parse(line):
        split_record = []
        split_record = line.split(",")
        if(len(split_record) != 1):
            return split_record[0],split_record[1],split_record[2]
        else:
            return [0,0,0]
    
    @staticmethod
    def readFile():
        path = "dataUser.txt"
        if(os.path.exists(path)):
            file = open(path,'r')
            records = file.read().split("\n")
            file.close()
            
            for line in records:
                username , password , role = MUserDL.parse(line)
                user = MUser(username,password,role)
                MUserDL.addUser(user)
                
            return True
        else:
            return True
    
    @staticmethod
    def storeFile():
        path = "dataUser.txt"
        file = open(path,'w')
        for storedUser in MUserDL.usersList:
            file.write(storedUser.username + "," + storedUser.password + "," + storedUser.role + "\n")
        file.close()
            