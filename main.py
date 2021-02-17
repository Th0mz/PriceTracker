from dataBase import *
from webScraper import *
from sys import argv

NUM_ARGS = 0
FUNC = 1
FILENAME = "database.pkl"

def updateDataBase():
    # For all products and each product website 
    # get its price and update the database

    for product in database.products:
        for info in product.info:
            price = float(scrape(info).replace(u'\xa0', "").replace("€", "").replace(",", "."))
            product.addNewPrice(price, info)

    database.changeMade()
    # Save modified database
    saveDataBase(FILENAME, database)

def printDataBase():
    print(database)

def printSpecificDataBase():
    # Prints the database which pathname is passed by argument
    specificDataBase = loadDataBase(argv[2])
    print(specificDataBase)


def updateAndPrintDataBase():
    updateDataBase()
    printDataBase()

def resetDataBase():
    global database
    # Save the old database in a newfile which name 
    # is passed by the command line (arg)
    saveDataBase(argv[2], database)

    # Reset the data base and save it on the default filename
    database = newDataBase()
    saveDataBase(FILENAME, database)

def forceResetDataBase():
    # Resents the database but doesn't save the old one
    database = newDataBase()
    saveDataBase(FILENAME, database)


def removeProduct():
    removed = database.removeProduct(argv[2])
    if not removed:
        print("Error : There is no product with that name")
    else:
        print(f"Successfully removed the product {argv[2]}")
        saveDataBase(FILENAME, database)

def removeInfo():
    removed = database.removeInfo(argv[2], argv[3])
    if not removed:
        print("Error : There is no product or info with that name")
    else:
        print(f"Successfully removed the info {argv[3]} of the product {argv[2]}")
        saveDataBase(FILENAME, database)

def addProduct():
    newProduct = Product(argv[2])
    database.addProduct(newProduct)
    saveDataBase(FILENAME, database)
    print("Product added successfully")

def addInfo():
    newInfo = Info(argv[3], None)
    added = database.addInfo(argv[2], newInfo)
    if not added:
        print("Error : There is no product with that name")
    else:
        print("Info added successfully")
        saveDataBase(FILENAME, database)

def addScrappingData():
    newScrappingData = ScrappingData(argv[4], argv[5], argv[6], argv[7])
    added = database.addScrappingData(argv[2], argv[3], newScrappingData)

    if not added:
        print("Error : Some of the given arguments arent valid")
    else:
        print("Scrapping Data added successfully")
        saveDataBase(FILENAME, database)

# Stores all the commands and the number of arguments for each command
commands = {
    "-p" :  [2, printDataBase],
    "-pn" : [3, printSpecificDataBase],
    "-up" : [2, updateAndPrintDataBase],
    "-r" :  [3, resetDataBase],
    "-fr" : [2, forceResetDataBase],
    "-rp" : [3, removeProduct],
    "-ri" : [4, removeInfo],
    "-ap" : [3, addProduct],
    "-ai" : [4, addInfo],
    "-as" : [8, addScrappingData]
}


# Load database from file
database = loadDataBase(FILENAME)
if (len(argv) == 1):
    # If there are no given arguments just update the database
    updateDataBase()
elif (argv[1] in commands.keys() and commands[argv[1]][NUM_ARGS] == len(argv)):
    # If the command exist and the number of arguments is valid execute the command
    commands[argv[1]][FUNC]()
    
else:
    raise NameError(f"Invalid Arguments.")
    