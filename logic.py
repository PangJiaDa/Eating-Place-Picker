from query import *
import datahandler
import random
import foodoption
import result

MESSAGE_INVALID_QUERY = "Invalid query."
MESSAGE_RANDOM_CHOICE = "Your random choice is:"
MESSAGE_ADD_FOOD_OPTION = "Your food option has been added."
MESSAGE_MODIFY_FOOD_OPTION = "Your food option has been modified."
MESSAGE_DELETE_FOOD_OPTION = "Your food option has been deleted."
MESSAGE_DISPLAY_ALL = "Here are all the food options:"

class Logic:

    def __init__(self):
        self.datahandler = datahandler.DataHandler()
        self.foodOptions = self.datahandler.getData()
    
    def saveChanges(self):
        self.datahandler.writeData(self.foodOptions)

    def processQuery(self, query):
        if isinstance(query, GetRandomFoodOptionQuery):
            return self.processGetRandomFoodOptionQuery(query)
        elif isinstance(query, AddFoodOptionQuery):
            return self.processAddFoodOptionQuery(query)
        elif isinstance(query, ModifyFoodOptionQuery):
            return self.processModifyFoodOptionQuery(query)
        elif isinstance(query, DeleteFoodOptionQuery):
            return self.processDeleteFoodOptionQuery(query)
        elif isinstance(query, DisplayAllQuery):
            return self.processDisplayAllQuery(query)
        else:
            print(MESSAGE_INVALID_QUERY)
            return None

    # returns a list containing the randomly selected option
    def processGetRandomFoodOptionQuery(self, query):
        return result.Result(MESSAGE_RANDOM_CHOICE, [random.choice(self.foodOptions)])

    # returns a list containing the newly added option
    def processAddFoodOptionQuery(self, query):
        self.foodOptions.append(self.extractFoodOption(query))
        return result.Result(MESSAGE_ADD_FOOD_OPTION, [self.foodOptions[-1]])

    # returns a list containing the modified option
    def processModifyFoodOptionQuery(self, query):
        #validate the index to modify
        if 0 <= query.selector < len(self.foodOptions):
            self.foodOptions[query.selector] = self.extractFoodOption(query)
        return result.Result(MESSAGE_MODIFY_FOOD_OPTION, [self.foodOptions[query.selector]])

    # returns an empty list
    def processDeleteFoodOptionQuery(self, query):
        #validate the index to modify
        if 0 <= query.selector < len(self.foodOptions):
            del self.foodOptions[query.selector]
        return result.Result(MESSAGE_DELETE_FOOD_OPTION, [])

    def processDisplayAllQuery(self, query):
        return result.Result(MESSAGE_DISPLAY_ALL, self.foodOptions)

    # extracts the FoodOption object from the query
    # query must be of type AddFoodOptionQuery or ModifyFoodOptionQuery
    def extractFoodOption(self, query):
        return foodoption.FoodOption(query.name, query.mealTimes, query.travelTime, query.categories)

# tests
# addQuery = AddFoodOptionQuery("char shao add", [1, 2], 100, [1, 2, 3, 4])
# modQuery = ModifyFoodOptionQuery(1000, "char shao modify", [2], 100, [1, 2, 3, 4])
# delQuery = DeleteFoodOptionQuery(0)
# logic = Logic()
# logic.processQuery(addQuery)
# logic.processQuery(modQuery)
# logic.processQuery(delQuery)
# print(logic.foodOptions)