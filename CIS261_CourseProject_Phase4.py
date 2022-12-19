#Nikah LeDet
#CIS261
#WK9 Course Project Phase4

def Login():
    UserFile = open("Users.txt", "r")
    UserList = []
    UserName = input("Enter User Name: ")
    UserRole = "None"
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            return UserRole, UserName
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        if UserName == UserList[0]:
            UserRole = UserList[2]
            return UserRole, UserName

