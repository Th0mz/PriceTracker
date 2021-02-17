from time import asctime as currentTime
import pickle

class ScrappingData:
    def __init__(self, website, tag, attribute, value):
        self.website = website
        self.tag = tag
        self.attribute = {attribute : value}

    def toString(self, xIndentation):
        indentation = "\t" * xIndentation
        return f"{indentation} - Website : {self.website}\n{indentation} - Tag : {self.tag}\n{indentation} - Attribute : {self.attribute}"

    def __str__(self):
        return self.toString(0)

class Info:
    def __init__(self, name, scrappingData):
        self.name = name
        self.scrappingData = scrappingData
        self.prices = []

    def addNewPrice(self, price):
        priceData = {
                "Price" : price,
                "Time" : currentTime()
        }

        self.prices.append(priceData)

    def toString(self, xIndentation):
        indentation = "\t" * xIndentation
        infoString = f"{indentation} - Name : {self.name}\n{indentation} - Scrapping Data : "

        if self.scrappingData:
            infoString += f"\n{self.scrappingData.toString(xIndentation + 1)}"
        else:
            infoString += "No Data"


        infoString += f"\n{indentation} - Prices :\n"
        for price in self.prices:
            infoString += f"\t{indentation} > {price}\n".replace("{", "").replace("}", "").replace("'", "") 
        
        return infoString 

    def __str__(self):
        return self.toString(0)

class Product:
    def __init__(self, name):
        self.name = name
        self.lowestPrice = -1
        self.info = []

    def addInfo(self, info):
        self.info.append(info)

    def addScrappingData(self, name, scrappingData):
        for info in self.info:
            if info.name == name:
                info.scrappingData = scrappingData
                return True

        return False

    def removeInfo(self, name):
        for info in self.info:
            if info.name == name:
                self.info.remove(info)
                return True

        return False

    def addNewPrice(self, price, info):
        if info not in self.info:
            return

        if (self.lowestPrice < 0 or self.lowestPrice > price ):
            self.lowestPrice = price
        
        info.addNewPrice(price)

    def toString(self, xIndentation):
        indentation = "\t" * xIndentation
        productString = f"{indentation} ====: Product :====\n{indentation} - Name: {self.name}\n{indentation} - Lowest Price : {self.lowestPrice}\n{indentation} - Info :\n" 

        for info in self.info:
            productString += f"{info.toString(xIndentation + 1)}\n\n"

        productString += f"{indentation} ====:=========:===="
        return productString

    def __str__(self):
        return self.toString(0)

class DataBase:
    def __init__(self):
        self.lastUpdate = currentTime()
        self.products = []
    
    def addProduct(self, product):
        self.products.append(product)

    def addInfo(self, productName, info):
        for product in self.products:
            if product.name == productName:
                product.addInfo(info)
                self.changeMade()
                return True

        return False

    def addScrappingData(self, productName, infoName, scrappingData):
        for product in self.products:
            if product.name == productName:
                added = product.addScrappingData(infoName, scrappingData)
                if added:
                    self.changeMade()

                return added

        return False


    def removeProduct(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                self.changeMade()
                return True

        return False

    def removeInfo(self, productName, infoName):
        for product in self.products:
            if product.name == productName:
                removed = product.removeInfo(infoName)
                if removed:
                    self.changeMade()

                return removed

        return False
    def changeMade(self):
        self.lastUpdate = currentTime()

    def __str__(self):
        dataBaseString = f"====: Data Base :====\n - Last Update : {self.lastUpdate}\n - Products : \n"

        for product in self.products:
            dataBaseString += f"{product.toString(1)}\n"
        dataBaseString += f"====:===========:====\n" 
        return dataBaseString


def newDataBase():
    database = DataBase()
    return database

def saveDataBase(filename, database):
    with open(filename, "wb") as output:
        pickle.dump(database, output, pickle.HIGHEST_PROTOCOL)

def loadDataBase(filename):
    database = None
    with open(filename, "rb") as input_:
        database = pickle.load(input_)

    return database
