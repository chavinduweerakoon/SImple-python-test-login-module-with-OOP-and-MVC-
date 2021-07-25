# controller / business logic
from dbcontext import mysqlconnection


class account:

    __connection = None

    def __init__(self):
        self.__connection = mysqlconnection.connect()

    def login(self, users):
        if self.__isvalidLogin(users):
            if self.__isAuthentic(users):
                self.__Authorize(users)
            else:
                users.setMessage("Incorrect username and password")
        else:
            users.setMessage("Please provide a username and password")

    def __isvalidLogin(self, users):
        if users.getUsername() != "" and users.getPassword() != "":
            return True
        return False

    def __isAuthentic(self, users):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT `userid` FROM `users` WHERE `username` = '" +
                       users.getUsername()+"' AND `password` = '"+users.getPassword()+"' ")
        record = cursor.fetchone()
        if record != None:
            return True
        return False

        # if users.getUsername() == "test" and users.getPassword() == "12345":
        #     return True
        # return False

    def __Authorize(self, users):
        users.setMessage(users.getUsername()+" is Logged In")


# accountObject = account()
# print(mysqlconnection.message)
