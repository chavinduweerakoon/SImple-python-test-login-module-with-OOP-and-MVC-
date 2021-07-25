# view
# import model as data
from model import users
from accountsController import account

dataObject = users()
validateObject = account()

print('---------Welcome--------------')

dataObject.setUsername(input("Please provide your Username: "))
dataObject.setPassword(input("Please provide your Password: "))

validateObject.login(dataObject)

print(dataObject.getMessage())

# print(dataObject.getUsername())
# print(dataObject.getPassword())
