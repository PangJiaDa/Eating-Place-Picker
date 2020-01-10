from query import *
import datahandler
import random
import foodoption

class Logic:

    def __init__(self):
        self.datahandler = datahandler.DataHandler()
        self.foodOptions = self.datahandler.getData()

    def processQuery(self, query):
        if isinstance(query, GetRandomFoodOptionQuery):
            self.processGetRandomFoodOptionQuery(query)
        elif isinstance(query, AddFoodOptionQuery):
            self.processAddFoodOptionQuery(query)
        elif isinstance(query, ModifyFoodOptionQuery):
            self.processModifyFoodOptionQuery(query)
        elif isinstance(query, DeleteFoodOptionQuery):
            self.processDeleteFoodOptionQuery(query)

    def processGetRandomFoodOptionQuery(self, query):
        return random.choice(self.foodOptions)

    def processAddFoodOptionQuery(self, query):
        self.foodOptions.append(self.extractFoodOption(query))

    def processModifyFoodOptionQuery(self, query):
        #validate the index to modify
        if 0 <= query.selector < len(self.foodOptions):
            self.foodOptions[query.selector] = self.extractFoodOption(query)

    def processDeleteFoodOptionQuery(self, query):
        #validate the index to modify
        if 0 <= query.selector < len(self.foodOptions):
            del self.foodOptions[query.selector]

    # extracts the FoodOption object from the query
    # query must be of type AddFoodOptionQuery or ModifyFoodOptionQuery
    def extractFoodOption(self, query):
        return foodoption.FoodOption(query.name, query.mealTimes, query.travelTime, query.categories)

    def getAllFoodOptions(self):
        return self.foodOptions

# tests
# addQuery = AddFoodOptionQuery("char shao add", [1, 2], 100, [1, 2, 3, 4])
# modQuery = ModifyFoodOptionQuery(1000, "char shao modify", [2], 100, [1, 2, 3, 4])
# delQuery = DeleteFoodOptionQuery(0)
# logic = Logic()
# logic.processQuery(addQuery)
# logic.processQuery(modQuery)
# logic.processQuery(delQuery)
# print(logic.foodOptions)